import json


def updating():
    def readData(_filename):
        with open(_filename, "r") as conn:
            return json.load(conn)

    data = readData("database.json")
    print("data read : ", data)

    oldpass = int(input("old password daxil edin : "))
    newpass = int(input("new password : "))

    for item in data['student']:
        if item['password'] == oldpass:
            item['password'] = newpass

    print("Melumat deyisdirildi...")
    print(data)

    with open("database.json", "w") as conn:
        json.dump(data, conn)
