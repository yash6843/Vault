import json
import random
import string

def write_json(new_data, filename='info.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["info"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def remove_json(query,filename='info.json'):
    with open(filename, 'r+') as file:
         data = json.load(file)
         search = False
         info = data["info"]
         for item in info:
              if query in item["title"]:
                    print("Query found!")
                    search = True
                    confirm = input("Do you want to delete this entry?\nEnter y for yes\nEnter n for no: ")
                    if(confirm == 'y'):
                          info.remove(item)
                          file.close()
                          with open(filename, 'w') as file:
                                         json.dump(data, file,indent = 4)
                                         return
         if(search != True):
               print("Query not found!")


def change_pin(pin="2024",filename='info.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["PIN"] = pin
        file.close()
    with open(filename, 'w') as file:
        json.dump(file_data, file,indent = 4)

def pass_gen(length=10):
    data = string.ascii_letters + string.digits + string.punctuation
    passw = ""
    for i in range(length):
        passw+=random.choice(data)
    
    return passw