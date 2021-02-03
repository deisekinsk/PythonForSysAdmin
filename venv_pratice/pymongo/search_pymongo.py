#!/usr/bin/env python3

from pymongo import MongoClient

mongo_con = MongoClient() #conexão
db = mongo_con["flask02-app"] #banco de dados

user = db.user.find_one(
    {
        "name":"Iara Freeley",
        "email":"Não tem"
    
    }
)

print(user)
print(user["_id"].generation_time)
