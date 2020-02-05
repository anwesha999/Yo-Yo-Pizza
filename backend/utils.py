import json

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