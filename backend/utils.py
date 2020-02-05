import json
import uuid

def load_data():
    with open('data.json') as json_file:
        data = json.load(json_file)
        return data

def save_data(obj):
    try:
        with open('data.json', 'w') as outfile:
            json.dump(obj, outfile)
            return True
    except Exception as e:
        print(e)
        return False


def add_new_user(obj):
    try:
        data = load_data()

        data["users"][obj["phoneNumber"]] = {
            "name" : obj["name"]
        }

        save_data(data)
        return True
    except:
        return False

def add_new_order(obj):
    try:
        data = load_data()

        unique_id = str(uuid.uuid1()).split("-")
        unique_id = unique_id[0][-4]+unique_id[3]
        unique_id = unique_id.upper()

        data["orders"][unique_id] = obj
        
        save_data(data)
        return unique_id
    except
        return False