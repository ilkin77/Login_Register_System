import json


def deleting():
    def readData(_filename):
        with open(_filename, "r") as conn:
            return json.load(conn)

    data = readData("database.json")
    print("data read : ", data)

    oldpass = int(input("old password daxil edin : "))

    for item in data['student']:
        if item['password'] == oldpass:
            data['student'].remove(item)


    print("Melumat silindi...")
    print(data)

    with open("database.json", "w") as conn:
        json.dump(data, conn)
