#!/usr/bin/env python3

from flask import Flask, Response
import json

from grupos.blueprint import grupos_routes
from mensagens.blueprint import mensagens_routes
from usuarios.blueprint import usuarios_routes

app = Flask (__name__)
app.register_blueprint(grupos_routes)
app.register_blueprint(usuarios_routes)
app.register_blueprint(mensagens_routes)

@app.route("/") #rotas
def index(): #views
    retorno = {
        "app":"Sistema de mensagens",
        "version":1.8
    }
    return Response(
        json.dumps(retorno),
        200,
        content_type="application/"
    
    )

    
if __name__ == "__main__":
    app.run(debug=True)
