import requests
import json

cotacoes = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
#cotacoes = requests.get("http://economia.awesomeapi.com.br/json/last/USDBRL") Response 404
cotacoes = cotacoes.json()
print(cotacoes)

dolar = cotacoes['USDBRL']['bid']
print(dolar)


#Create a free Firebase DB
#CRUD (create read update delete)
#requests (GET / POST / PATCH / DELETE)

#GET
BD = requests.get("https://teste-d892c-default-rtdb.firebaseio.com/.json")
print(BD.json())
BD = BD.json()
print(BD[0])

#POST
info = '{"Nome": "Anderson"}'
BD2 = requests.post("https://teste-d892c-default-rtdb.firebaseio.com/.json", data = info)
print(BD2)
print(BD2.json())

#PATCH
info = '{"Idade": "20"}'
BD3 = requests.patch("https://teste-d892c-default-rtdb.firebaseio.com/-Ms_SA2QwYED_4Q_FdKW.json", data = info)
print(BD3)
print(BD3.json())

#DELETE
requests = requests.delete("https://teste-d892c-default-rtdb.firebaseio.com/-Ms_SA2QwYED_4Q_FdKW/Nome.json")