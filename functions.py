import json

# data read to json
def readData():
    with open("database.json", "r") as conn:
        return json.load(conn)




# show student information by name

def reading():
    user_name = input("Telebe adini daxil edin : ")
    readData()
    data = readData()
    for item in data['student']:
        if user_name == item['name']:
            print(item)
            break
    else:
        print(f"A student named {user_name} was not found in the database")


#reading()
