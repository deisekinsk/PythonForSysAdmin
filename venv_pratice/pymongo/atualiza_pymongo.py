#!/usr/bin/env python3

from pymongo import MongoClient

mongo_con = MongoClient() #conexão
db = mongo_con["flask02-app"] #banco de dados

user = db.user.update_one(
    {
        "name":"Iara Freeley",
        "email":"iara@gmail.com"
    
    },
    {
        "$set":{
            "email":"iara02@gmail.com"
        }
    
    }
)

print(user.matched_count,user.modified_count)
