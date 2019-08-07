import json
from pprint import pprint

name_to_group = {}
groups_counters = {}

database_path = "assets/database.json"


def dump(json_data):
    with open(database_path,'w') as f:
        json.dump(json_data, f)


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


def update_user_status(user, status, json_data):
    global groups_counters
    if user not in name_to_group.keys():
        raise IndexError
    # TODO: validate status
    group_name = name_to_group[user]
    if json_data[group_name[::-1]][user[::-1]]['status'] == "":
        groups_counters[group_name] += 1
    json_data[group_name[::-1]][user[::-1]]['status'] = status
    dump(json_data)

def is_group_reported(user, json_data):
    group_name = name_to_group[user]
    return groups_counters[group_name] == len(json_data[group_name[::-1]]), group_name


def clear_statuses(json_data):
    for group, people in json_data.items():
        for person, _ in people.items():
            json_data[group][person]['status'] = ""
    dump(json_data)
        