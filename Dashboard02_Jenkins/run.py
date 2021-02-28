#!/usr/bin/env pyhton3

from flask import Flask, render_template
from R_jenkins.blueprint import jenkins_routes
from R_docker.blueprint import docker_routes

app = Flask(__name__)
app.register_blueprint(jenkins_routes)
app.register_blueprint(docker_routes)

@app.route("/")
def index():
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True)
