import json

def read_users_and_groups():
    with open('assets/database.json','r') as f:
        return json.load(f)

def initialize_group_counter(json):
    groups_counters = {}
    for group in json: 
        groups_counters[group['name']] = 0
    return groups_counters
