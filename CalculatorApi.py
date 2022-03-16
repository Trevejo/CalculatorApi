from ast import operator
import json, requests
from urllib import response

operator = input("Enter integrate, derive, simplify etc: ")
equation = input("Enter equation: ")

url = "https://newton.now.sh/api/v2/" + operator + "/" + equation

response = requests.get(url)

data = json.loads(response.text)

print("The result is ", data['result'])

input("press enter to exit")