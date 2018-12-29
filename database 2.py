import json

def set_value(value, key):
    file = open("file.json", "w")
    json.dump({key: value}, file)
    file.close()

def get_value(key):
    file = open("file.json", "r")
    info = json.load(file)
    if key in info:
        return info[key]
    else: return None
    file.close()
