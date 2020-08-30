import json

user_name = input("Telebe adini daxil edin : ")

def reading():
    def readData(_filename):
        with open(_filename, "r") as conn:
            return json.load(conn)

    data = readData("database.json")
    for item in data['student']:
        if user_name == item['name']:
            print(item)

reading()