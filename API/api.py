import requests
import json

cotacoes = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
#cotacoes = requests.get("http://economia.awesomeapi.com.br/json/last/USDBRL") Response 404
code=cotacoes.status_code
assert code==200, "Request Failed"
print(cotacoes.json()['USDBRL']['bid'])
assert cotacoes.json()['USDBRL']['code']=='USD'
print(code)
#print(cotacoes.text)
#print(cotacoes.content)
#print(cotacoes.headers)

cotacoes = cotacoes.json()
print(cotacoes)

dolar = cotacoes['USDBRL']['bid']
print(dolar)

#Working with params
#p = {"moedas":"USD-BRL"}
#response = requests.get("http://economia.awesomeapi.com.br/",params=p)
#print(response.url)

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

#PATCH (selected values) / PUT (all values)
info = '{"Idade": "20"}'
BD3 = requests.patch("https://teste-d892c-default-rtdb.firebaseio.com/-Ms_SA2QwYED_4Q_FdKW.json", data = info)
print(BD3)
print(BD3.json())

#DELETE
requests = requests.delete("https://teste-d892c-default-rtdb.firebaseio.com/-Ms_SA2QwYED_4Q_FdKW/Nome.json")

#TIMEOUT
r= requests.get("https://httpbin.org/delay/1", timeout=3)
print(r.status_code)

#AUTHENTICATION
response = requests.get("https://the-internet.herokuapp.com/basic_auth",auth=('admin','admin'))
print(response.status_code)