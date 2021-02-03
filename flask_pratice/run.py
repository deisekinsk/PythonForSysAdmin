from flask import Flask,render_template,jsonify,request
from pymongo import MongoClient
import json
from Blueprints.UsuariosView import usuarios
from Models.Model import app, db

app.register_blueprint(usuarios)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/chamado/<numero>/")
def chamado(numero):
    return render_template("chamado.html")

@app.route("/provisionamento/")
def provisionamento():
    return render_template("provisionamento.html")

@app.route("/provisionamento/novo/",methods=["POST"])
def provisionamento_novo():
    try:
        j = json.loads(request.get_json())
        j["gitlab"]["desenvolvedores"] = j["gitlab"]["desenvolvedores"].split(",")
        j["jenkins"]["branches"] = j["jenkins"]["branches"].split(",")
        j["docker"] = j["docker"].split(",")
        client = MongoClient("127.0.0.1")
        db = client["dexterops"]
        db.provisionamento.insert(j)
        return jsonify({"message":"Inserido no banco com sucesso"})
    except Exception as e:
        return jsonify({"message":"%s"%e})

@app.route("/provisionamento/lista/")
def provisionamento_lista():
    try: 
        client = MongoClient("127.0.0.1")
        db = client["dexterops"]
        lista = db.provisionamento.find({"_id":1})[0]
        return jsonify(lista)
    except Exception as e:
        return jsonify({"message":"%s"%e})

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True,host="0.0.0.0")

