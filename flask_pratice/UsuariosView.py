#!/usr/bin/python

from flask import Blueprint,jsonify,request
from Models.Model import db,Usuarios

usuarios = Blueprint('usuarios',__name__)

@usuarios.route("/usuarios/")
def usuarios_listar():
    try:        
        users = Usuarios.query.all()
        dic = {"usuarios":[]}
        for u in users:
            dic['usuarios'].append({"id":u.id,"nome":u.nome,"email":u.email})
        return jsonify(dic)
    except Exception as e:
        return jsonify({"status":1,"message":"Ocorreu um erro: %s"%e})

@usuarios.route("/usuarios/",methods=["POST"])
def usuarios_cadastrar():
    try:
        res = request.get_json()
        user = Usuarios(res['nome'],res['email'])
        db.session.add(user)
        db.session.commit()
        return jsonify({"message":"Usuario cadastrado com sucesso"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"status":1,"message":"Ocorreu um erro: %s"%e})

@usuarios.route("/usuarios/<int:id>/",methods=["PUT"])
def usuarios_atualizar(id):
    try:
        user = Usuarios.query.filter(Usuarios.id==id).first()
        dados = request.get_json()
        for k in dados.keys():
            setattr(user,k,dados[k])
        db.session.commit()
        user = Usuarios.query.filter(Usuarios.id==id).first()
        user.__dict__.pop("_sa_instance_state",None)
        return jsonify(user.__dict__)
    except Exception as e:
        db.session.rollback()
        return jsonify({"status":1,"message":"Ocorreu um erro: %s"%e})

@usuarios.route("/usuarios/<int:id>/",methods=["DELETE"])
def usuarios_deletar(id):
    try:
        user = Usuarios.query.filter(Usuarios.id==id).first()
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message":"Usuario deletado com sucesso!"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"status":1,"message":"Ocorreu um erro: %s"%e})

@usuarios.route("/usuarios/<int:id>/")
def usuarios_encontrar(id):
    try:
        user = Usuarios.query.filter(Usuarios.id==id).first()
        user.__dict__.pop("_sa_instance_state",None)
        return jsonify(user.__dict__)
    except Exception as e:
        return jsonify({"status":1,"message":"Ocorreu um erro: %s"%e})
