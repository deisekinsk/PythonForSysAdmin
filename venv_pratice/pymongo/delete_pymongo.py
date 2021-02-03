#!/usr/bin/env python3

from pymongo import MongoClient

mongo_con = MongoClient() #conexão
db = mongo_con["flask02-app"] #banco de dados

deleted = db.user.delete_one(
    {
        "name":"Iara Freeley"
    }
)

print(deleted.deleted_count)
