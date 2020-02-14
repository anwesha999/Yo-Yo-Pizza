import json
import uuid
import os
from datetime import datetime

def create_datafile():
    data = {
        "orders":{},
        "users":{}
    }
    save_data(data)

def load_data():
    json_file = open('data.json')
    data = json.load(json_file)
    json_file.close()
    return data

def save_data(obj):
    try:
        json_file  = open('data.json', 'w')
        json.dump(obj, json_file)
        json_file.close()
        return True
    except Exception as e:
        print(e)
        return False


def update_user_info(obj):
    try:
        data = load_data()

        user_id = obj["phoneNumber"]

        data["users"][user_id] = {}
        
        for key in obj.keys():
            data["users"][user_id][str(key)] = obj[key] 

        save_data(data)
        return True
    except Exception as e:
        print(e)
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
    except:
        return False

def order_status(order_id):
    data = load_data()
    if order_id in data["orders"].keys():
        placedAt = datetime.fromtimestamp(data["orders"][order_id]["placedAt"])
        now = datetime.now()
        minutes = (now - placedAt).total_seconds()/60
        if minutes < 15 :
            return "Preparing"
        elif minutes >=15 and minutes <=30:
            return "Out for delivery"
        else:
            return "Delivered" 
    else:
        print("not present")


if not "data.json" in os.listdir("./"):
    create_datafile()