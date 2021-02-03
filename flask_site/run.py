#!/usr/bin/env pyhton3

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
    "index.html",
    title= "Frutas",
    varNomes=[
        "Banana",
        "Maçã",
        "Laranja",
        "Melancia"
    ]
    )
    
if __name__ == "__main__":
    app.run(debug=True)
