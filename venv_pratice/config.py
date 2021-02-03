#!/usr/bin/env python3

from pymongo import MongoClient #importando a classe

mongo_con = MongoClient() #conexão
mongo_db = mongo_con["flask02-app"]#escolhendo o banco de dados
