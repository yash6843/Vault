import json
import random
import string
import webbrowser
import cryptocode 
import py7zr
import os

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

def transcript(filename='info.json', pin='2024'):
    with open('info.json', "r") as f:
         fa = json.load(f)
         data = fa["info"]
    with open('transcript.txt', "a") as f:
         f.write("Format: title , username , password\n")
         for i in range(len(data)):
              f.write(data[i]["title"]+' , '+cryptocode.decrypt(data[i]["username"],"mypassword")+' , '+cryptocode.decrypt(data[i]["password"],"mypassword")+"\n")

    with py7zr.SevenZipFile('Vault.7z', 'w', password=str(pin)) as archive:
        if(os.path.exists('./Vault.7z/transcript.txt')):
             os.remove('./Vault.7z/transcript.txt')
        archive.write('transcript.txt')
    os.remove('transcript.txt')
    webbrowser.open("Vault.7z")