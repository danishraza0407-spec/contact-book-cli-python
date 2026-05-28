import json
file_name = "data.json"

try:
    with open(file_name , "r") as file:
        contacts = json.load(file)


except:
    contacts = []

def update_file():
    with open(file_name ,"w") as file:
        json.dump(contacts , file)

while(1):
    print("1. add the contact")
    print("2. show the contact")
    print("3. search contact")
    print("4. delete contact")
    print("5. exit")
    choice = input("enter you number to want :")
    if(choice == "1"):
        name = input("enter the name : ")
        number = input("enter the contact number :")
        contact = {
            "name" : name,
            "number" : number
        }
        contacts.append(contact)
        update_file()
        print("--contect add succesfull--")
    elif(choice == "2"):
        if(len(contacts)==0):
            print("--no data available--")
        else:
            print("--contect details--\n")
            for contact in contacts:
                print("----------------------------")
                print("name : " ,contact["name"])
                print("number : ",contact["number"])
                print("-----------------------------")
    elif(choice == "3"):
        found = 0
        search = input("enter the number search :")
        for contact in contacts :
            if(contact["number"]==search):
                print("------------------------------")
                print("name : ",contact["name"])
                print("number : ",contact["number"])
                print("------------------------------")
                print("**you search successfully**")
                found = 1
        if(found == 0):
            print("data not available in list")
    elif(choice == "4"):
        found = 0
        search = input("enter the number to delete :")
        for contact in contacts :
            if(contact["number"] == search):
                contacts.remove(contact)
                update_file()
                print("--delete the contact successfully--")
                found = 1
                break                   
        if(found == 0):
            ("not available this number")
    elif(choice == "5"):
        print("now you exit of system ")
        break
    else:
        print("enter valid number ")  

    
                    
