import json
import re

with open('data.csv', "r") as file:
    data = file.read()


lista = []

for item in data.split("\n"):

    diccionario = {}
    headers = ["date", "name", "title", "price", "quantity"]

    fields = item.split(",")

    for i in range(len(fields)):
        diccionario[headers[i]] = fields[i]

    lista.append(diccionario)


print(lista)




with open('./data.json') as file:
    data = file.read()
    data_json = json.loads(data)
    data_json = json.dumps(data_json, indent=4)


print(data_json)
print(type(data_json))
