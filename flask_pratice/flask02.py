#!/usr/bin/env python3

from flask import Flask
app = Flask (__name__)

@app.route("/flask02/<int:id>") #rotas
def hello(id): #views
    return "Funcionou., %s" %(id)
    
@app.route("/teste") #Nova rota
def teste(): #views
    return "Entrando nova rota."
    
if __name__ == "__main__":
    app.run(debug=True)
