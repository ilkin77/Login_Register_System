from login import *
from register import *
from time import sleep

print("""Welcome teacher :)
Login    -> 1
register -> 2
""")



def start():
    order = int(input("Choose your number : "))
    try:
        if order == 1:
            username = input("Username : ")
            password = int(input("Password : "))
            with open("database.json", "r") as conn:
                data = json.load(conn)
                for item in data['teachers']:
                    if item['username'] == username and item['password'] == password:
                        print("Please waiting...")
                        sleep(2)
                        print("Succesfull :)")
                        login()
                        break
                else:
                    print("Invalid username or password")
        elif order == 2:
            register()
        else:
            print("Please enter 1 or 2")
    except:
        print("An error occurred")




start()