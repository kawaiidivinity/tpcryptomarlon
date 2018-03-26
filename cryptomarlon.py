#!/usr/bin/python2.6
import requests

print("Bonjour !\n")
print("Quel est ton choix de cryptomonnaie ?\n")
crypto = input("Entrez un nom :\n")
response = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+crypto+"&tsyms=EUR")
print(response.text)
