import json


def reading():
    def readData(_filename):
        with open(_filename, "r") as conn:
            return json.load(conn)

    data = readData("database.json")
    # print("data : ", data)

    for item in data['student']:
        print(f"Name : {item['name']} \nSurname :  {item['surname']} \n"
              f"Age :  {item['age']} \nUsername : {item['username']} \nPassword : {item['password']} \n")

