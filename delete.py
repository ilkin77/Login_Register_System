import json
from functions import readData
from time import sleep

def deleting():
    readData()

    data = readData()
    #print("data read : ", data)

    oldpass = int(input("write password : "))

    for item in data['student']:
        if item['password'] == oldpass:
            data['student'].remove(item)

    sleep(2)
    print("Melumat silindi...")
   # print(data)

    with open("database.json", "w") as conn:
        json.dump(data, conn)
