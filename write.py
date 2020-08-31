import json
from functions import readData



def Writing():

    readData()

    data = readData()
    #print("data : ", data)

    def getDataFromUser():
        print("Add student")
        name = input("name : ")
        surname = input("surname : ")
        age = int(input("age : "))
        username = input("username : ")
        password = int(input("password : "))


        students = {
            "name": name,
            "surname": surname,
            "age": age,
            "username": username,
            "password": password
        }
        data['student'].append(students)

    num = int(input("Elave edilecek telebe sayini yazin : "))

    for i in range(num):
        getDataFromUser()

    with open("database.json", "w") as conn:
        json.dump(data, conn)

