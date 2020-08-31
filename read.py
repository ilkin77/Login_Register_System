import json
from functions import readData

def reading():

    readData()
    data = readData()

    print("""Student information -> 1
Teachers information 2""")
    info = int(input("press 1 or 2 : "))

    if info == 1:
        for item in data['student']:
            print(f"Name : {item['name']} \nSurname :  {item['surname']} \n"
                  f"Age :  {item['age']} \nUsername : {item['username']} \nPassword : {item['password']} \n")
    elif info == 2:
        for item in data['teachers']:
            print(f"Name : {item['name']} \nSurname :  {item['surname']} \n"
                  f"Username : {item['username']} \nPassword : {item['password']} \n")

