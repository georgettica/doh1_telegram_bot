import json
from modules.constants import on_board_statuses, off_board_statuses
from modules.exceptions.no_username import NoUsername
from modules.exceptions.unknown_status import UnknownStatus
import os
from pathlib import Path

name_to_group = {}
groups_counters = {}

database_path = os.path.join(Path(os.path.dirname(__file__)).parent, 'assets/database.json')


def dump(json_data):
    with open(database_path,'w') as f:
        json.dump(json_data, f, ensure_ascii=False)


def read_users_and_groups():
    with open(database_path,'r') as f:
        return json.load(f)


def initialize(json_data):
    global groups_counters
    for group in json_data.keys(): 
        groups_counters[group[::-1]] = 0
    map_name_to_group(json_data)
    clear_statuses(json_data)


def map_name_to_group(json_data):
    global name_to_group
    for group, people in json_data.items():
        for person in people.keys():
            name_to_group[person[::-1]] = group[::-1]


def update_user_status(user, status, user_telegram_id, json_data):
    global groups_counters
    if user not in name_to_group.keys():
        raise NoUsername
    if status not in on_board_statuses and status not in off_board_statuses:
        raise UnknownStatus
    group_name = name_to_group[user]
    parsed_group_name = group_name[::-1]
    parsed_user_name = user[::-1]
    user = json_data[parsed_group_name][parsed_user_name]
    if 'is_leader' in user:
        user["telegram_id"] = user_telegram_id
    if user['status'] == "":
        groups_counters[group_name] += 1
    user['status'] = status
    dump(json_data)


def is_group_reported(user, json_data):
    group_name = name_to_group[user]
    return groups_counters[group_name] == len(json_data[group_name[::-1]]), group_name[::-1]


def clear_statuses(json_data):
    for group, people in json_data.items():
        for person, _ in people.items():
            json_data[group][person]['status'] = ""
    dump(json_data)


def get_leader_telegram_id(group_name, json_data):
    for person in json_data[group_name].values():
        if "is_leader" in person:
            return person["telegram_id"]


def get_unreported(json_data):
    unreported = []
    for group in json_data.values():
        for person_name, person in group.items():
            if person["status"] == "":
                unreported.append(person_name)
    return unreported


def display_unreported(json_data):
    unreported = get_unreported(json_data)
    return "The following people have not reported yet:\n" + "\n".join(unreported)


def ask_for_report(json_data):
    unreported = get_unreported(json_data)
    return "The following please report now:\n" + "\n".join(unreported)


def get_percentage_of_unreported(json_data):
    total = len(name_to_group)
    reported_amount = total - len(get_unreported(json_data))
    return  "Until now {0}% of the people have reported the status.". format(100*float(reported_amount)/total)
