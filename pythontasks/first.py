import json

with open("data.json","w")as file:
    json.dump(data,file)
    print("data svaed")

with open("data.json", "r")as file:
    loded_Data=json.load(file)
    print("loded file", loded_Data)
    