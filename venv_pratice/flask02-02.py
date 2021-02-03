#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, Response, request
import json
app = Flask (__name__)

@app.route("/jsonify") #rotas
def opt_jsonify(): #views
    retorno = { #Dicionário
        "message": "Usou jsonify"
    
    }
    return jsonify(retorno)
    
@app.route("/make_response") #rotas
def opt_make_response(): #views
    headers = {
        "content-type": "application/json"
    }
    
    retorno = { #Dicionário
        "message": "Usou make response"
    }
    return make_response(json.dumps(retorno),201,headers) #posso controlar a resposta

@app.route("/response") #rotas
def opt_response(): #views
    retorno = { #Dicionário
        "message": "Usou response"
    
    }
    return Response(json.dumps(retorno),404,content_type="application/json")


@app.route("/request", methods=["POST"]) #rotas
def opt_request(): #views
    retorno = request.get_json()
    return Response(json.dumps(retorno),200,content_type="application/json")
    
if __name__ == "__main__":
    app.run(debug=True)
