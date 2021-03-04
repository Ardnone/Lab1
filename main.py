import requests
import time
import json

d = {}
d1 = {}

def kurs():
    link = "https://blockchain.info/ru/ticker"
    return requests.get(link).text

d = kurs()
print(d)
vvod = input("Выберите валюту: ")
d = json.loads(kurs())
d1 = d[vvod]
print("Стоимость покупки биткоина в заданной валюте",vvod, "будет равна: ",d1)
