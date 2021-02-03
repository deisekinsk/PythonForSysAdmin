#! /usr/bin/env python3

from pymongo import MongoClient

mongo_con = MongoClient() #conexão
db = mongo_con["flask02-app"] #banco de dados

inserted = db.user.insert_one(
    {
        "name":"Iara Freeley",
        "email":"Não tem",
        "messages": [ #array com dicionário
            {
                "name":"nome_user",
                "message":"Mensagem Aqui"
            }
        ]
    }
)

print(inserted)
