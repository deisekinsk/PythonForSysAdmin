from flask import Blueprint
import json

grupos_routes = Blueprint(
    "grupos",
    __name__,
    url_prefix="/grupos"
)

@grupos_routes.route("")
def getGrupos():
    return "Acessou grupos"
