import maskpass # Hide/mask pass in prompt
import functions as fn # Basic functions for writing/reading json files
import json 
from pyfiglet import Figlet # Text art 
import cryptocode # for encryption and decryption

f = Figlet(font='slant')
print(f.renderText('Vault'))

passcode = maskpass.askpass("Please enter the login PIN: ")
with open("info.json","r") as f:
    pn = (json.load(f))["PIN"]

if(pn == passcode):
    option = "0"

    while option != "7": 
         print("\nPassword manager menu:\n1. Add entry\n2. Remove entry\n3. Search entry\n4. List all entries\n5. Change log-in PIN\n6. Password Generator\n7. Transcript all (Makes a encrypted zip file Vault.7z with all the data)\n8. Quit")
         option = input()
         
         if(option == "1"):
            title=input("Enter title: ")
            username=input("Enter username: ")
            passw=input("Enter password: ")
            dict = {
                "title": title,
                "username": cryptocode.encrypt(username,"mypassword"),
                "password": cryptocode.encrypt(passw,"mypassword")
            }
            fn.write_json(dict,filename="info.json")
        
         if(option == "2"):
             query = input("Enter the query/title you want to delete: ")
             fn.remove_json(query,filename='info.json')

         if(option == "3"):
            with open("info.json","r") as f:
                 search = False
                 query = input("Enter search query: ")
                 data = (json.load(f))["info"]
                 for i in range(len(data)):
                     if(query in data[i]["title"]):
                      search = True
                      print("Title:"+data[i]["title"]+"\nUsername:"+cryptocode.decrypt(data[i]["username"], "mypassword")
+"\nPassword:"+cryptocode.decrypt(data[i]["password"], "mypassword"))
                      print("------------------")
                 if(search != True): 
                  print("No entries found!!")

         if(option == "4"):
             print("------------------")
             with open("info.json","r") as f:
                 data = (json.load(f))["info"]
                 for i in range(len(data)):
                      print("Title:"+data[i]["title"]+"\nUsername:"+cryptocode.decrypt(data[i]["username"], "mypassword")+"\nPassword:"+"{ hidden }")
                      print("------------------")

         if(option == "5"):
             new_pin = input("Enter new PIN: ")
             fn.change_pin(new_pin,filename="info.json")
        
         if(option == "6"):
             length = int(input("Enter the length of password you want to generate: "))
             password = fn.pass_gen(length)
             print(password)

         if(option == "7"):
             ask = input("Are you sure you want to get all entries in a file? (y/n): ")
             if(ask.lower() == 'y' or ask.lower() =='yes'):
                 passcode =  maskpass.askpass("Enter the password you would like to encrypt the file with: ")
                 fn.transcript('info.json',passcode)
         if(option == "8"):
             break
else:
    print("WRONG PIN")