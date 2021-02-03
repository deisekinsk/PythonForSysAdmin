#!/usr/bin/env python3
#adicionando usuários
from flask import Blueprint, request, Response
from config import mongo_db #importa banco de dados
from bson.json_util import dumps #pymongo usa bson

usuarios_routes = Blueprint(
    "usuarios",
    __name__,
    url_prefix="/usuarios"
)

@usuarios_routes.route("")
def getUsuarios(): #Lista Usuários
    try:
        users = mongo_db.user.find()
        return Response(dumps(users),
        status=200,
        content_type="application/json"
        )
    except Exception as e:
        return "Erro: %s"%(e)

@usuarios_routes.route("", methods=["POST"])
def postUsuarios(): #Adiciona usuário
    try:
        user = request.get_json() #utiliza request do flask | Transforma de bson para dicionário
        mongo_db.user.insert_one( #função do pymongo insert_one
            {
                "name":user["name"],
                "email":user["email"],
                "messages": [ ] #array vazio
            }
        )
        response = {
        "message": "Usuário '%s' criado com sucesso!" % (user["name"])
        
        } #classe response | criar uma resposta
        return Response (
            dumps(response),
            status=201,
            content_type="application/json"
        )
    except Exception as e:
        return "Erro: %s"%(e)
        
@usuarios_routes.route("", methods=["PATCH"])
def updateUsuarios(): #Atualiza Usuários
    try:
        user = request.get_json() #recupera os dados
        update = mongo_db.user.update_one( #atualiza
            {"email": user["email"]}, #critério para localizar o usuário
            {"$set":user}
        )
        if update.modified_count:
            response = {"message":"Usuário '%s' atualizado com sucesso!"%(user["name"])}
            return Response (
            dumps(response),
            status=200,
            content_type="application/json")
            
        elif update.matche_count:
            response = {"message":"Usuário '%s' encontrado. Não atualizou."%(user["name"])}
            return Response (
            dumps(response),
            status=400,
            content_type="application/json")
            
        else:
            response = {"message": "Usuário '%s' não encontrado."%(user["email"])}
            return Response (
            dumps(response),
            status=404,
            content_type="application/json")
            
    except Exception as e:
        return "Erro: %s"%(e)

@usuarios_routes.route("", methods = ["DELETE"])
def deleteUsuarios(): #deleta usuário
    try:
        user = request.get_json()
        delete = mongo_db.user.delete_one(
            {"email": user["email"]}
        )
        if delete.deleted_count:
            response = {"message":"Usuário'%s'removido com sucesso!"%(user["email"])}
            return Response(
                dumps(response),
                status= 200,
                content_type = "application/json"
            )
        else:
            response = {"message":"Usuário '%s' não encontrado."%(user["email"])}
            return Response(
                dumps(response),
                status = 404,
                content_type="application/json"
            )
    except Exception as e:
        return "Erro: %s"%(e)
            
