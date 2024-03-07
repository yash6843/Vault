import maskpass # Hide/mask pass in prompt
import functions as fn # Basic functions for writing/reading json files
import json 
from pyfiglet import Figlet # Text art 

f = Figlet(font='slant')
print(f.renderText('Vault'))

passcode = maskpass.askpass("Please enter the 4 digit PIN: ")
with open("info.json","r") as f:
    pn = (json.load(f))["PIN"]
    
if(pn == passcode):
    print("Logged in")
    option = "0"

    while option != "5":
         print("[1] Add entry\n[2] Search entry\n[3] List all entries\n[4] Change log-in PIN\n[5] Quit")
         option = input()
         if(option == "1"):
            title=input("Enter title: ")
            username=input("Enter username: ")
            passw=input("Enter password: ")
            dict = {
                "title": title,
                "username": username,
                "password": passw
            }
            fn.write_json(dict,filename="info.json")

         if(option == "2"):
            with open("info.json","r") as f:
                 search = False
                 query = input("Enter search query: ")
                 data = (json.load(f))["info"]
                 for i in range(len(data)):
                     if(query in data[i]["title"]):
                      search = True
                      print("Title:"+data[i]["title"]+"\nUsername:"+data[i]["username"]+"\nPassword:"+data[i]["password"])
                      print("------------------")
                 if(search != True): 
                  print("No entries found!!")

         if(option == "3"):
             print("------------------")
             with open("info.json","r") as f:
                 data = (json.load(f))["info"]
                 for i in range(len(data)):
                      print("Title:"+data[i]["title"]+"\nUsername:"+data[i]["username"]+"\nPassword:"+data[i]["password"])
                      print("------------------")

         if(option == "4"):
             new_pin = input("Enter new PIN: ")
             fn.change_pin(new_pin,filename="info.json")
         if(option == "5"):
             break