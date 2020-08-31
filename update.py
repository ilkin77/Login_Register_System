import json
from functions import readData
from time import sleep

def updating():
    readData()

    data = readData()
    #print("data read : ", data)

    oldpass = int(input("old password daxil edin : "))
    newpass = int(input("new password : "))

    for item in data['student']:
        if item['password'] == oldpass:
            item['password'] = newpass

    sleep(2)
    print("Melumat deyisdirildi...")

    with open("database.json", "w") as conn:
        json.dump(data, conn)

