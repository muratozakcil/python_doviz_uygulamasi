import requests

api_key = "sizin_api_keyiniz"

url = "http://data.fixer.io/api/latest?access_key=" + api_key

first_currency = input("Birinci Para Birimi:")

second_currency = input("İkinci Para Birimi:")

amount = int(input("Miktar:"))

response = requests.get(url)

data = response.json()

firstValue = data["rates"][first_currency]
secondValue = data["rates"][second_currency]

print((secondValue / firstValue) * amount)
