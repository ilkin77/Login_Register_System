import json

def register():
    print("You must register to view student information.")
    qerar = input("Press 1 to continue, otherwise press 2 : ")
    if qerar == "1":
        WritingTeacher()
    else:
        print("Bye!")


def WritingTeacher():
    def readData(_filename):
        with open(_filename, "r") as conn:
            return json.load(conn)

    data = readData("database.json")
    print("data : ", data)

    def getDataFromUser():
        print("Register teacher : ")
        name = input("name : ")
        surname = input("surname : ")
        username = input("username : ")
        password = int(input("password : "))


        teacher = {
            "name": name,
            "surname": surname,
            "username": username,
            "password": password
        }
        data['teachers'].append(teacher)
    getDataFromUser()

    with open("database.json", "w") as conn:
        json.dump(data, conn)
