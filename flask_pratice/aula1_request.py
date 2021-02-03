import requests
#quarta parte DELETE

data = {
    "nome": "Dandara",
    "sobrenome": "hummel"
}

requisicao = requests.delete(
    "http://httpbin.org/delete",
    json=data,
)

json_to_dict = requisicao.json()
print(json_to_dict)
