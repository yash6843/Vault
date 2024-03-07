import json
def write_json(new_data, filename='info.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["info"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
def change_pin(pin="2024",filename='info.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["PIN"] = pin
        file.close()
    with open(filename, 'w') as file:
        json.dump(file_data, file,indent = 4)
