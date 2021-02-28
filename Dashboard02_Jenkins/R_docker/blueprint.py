from flask import Blueprint, render_template, redirect, url_for
import docker

docker_routes = Blueprint(
                "docker",
                __name__,
                url_prefix= "/docker"
                )
                
@docker_routes.route("")
def index():
    try:
        docker_con = docker.DockerClient("192.168.0.200:2376")
        container = docker_con.containers.get("flask-app")
        flask_app = {
            "id": container.short_id,
            "image": container.image.tags[0],
            "nome": container.name,
            "status": container.status
        }
    
    except Exception as e:
        flask_app = None
    
    return render_template(
        "docker.html",
        container = flask_app
    )

@docker_routes.route("/start")
def start():
    try:
        docker_con = docker.DockerClient("192.168.0.200:2376")
        container = docker_con.containers.get("flask-app")
        container.start()
        
    except Exception as e:
        pass
    return redirect (url_for("docker.index"))
    
@docker_routes.route("/stop")
def stop():
    try:
        docker_con = docker.DockerClient("192.168.0.200:2376")
        container = docker_con.containers.get("flask-app")
        container.stop()
        
    except Exception as e:
        pass
    return redirect (url_for("docker.index"))
