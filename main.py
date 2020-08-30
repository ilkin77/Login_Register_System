from login import *
from register import *

print("""Welcome teacher :)
Login    -> 1
register -> 2
""")

order = int(input("Choose your number : "))

try:
    if order == 1:
        username = input("Username qeyd edin : ")
        password = int(input("Password qeyd edin : "))
        with open("database.json", "r") as conn:
            data = json.load(conn)
            for item in data['teachers']:
                if item['username'] == username and item['password'] == password:
                    print("Zehmet olmasa biraz gozleyin...") #zaman elave et biraz gec yazilsin
                    print("Succesfull....")
                    login()
                else:
                    print("duzgun deyil bu hisseni duzeltmek laizmdir")
    elif order == 2:
        register()
    else:
        print("duzgun reqem yazmadiniz.")
except:
    print("Xeta bas verdi")
