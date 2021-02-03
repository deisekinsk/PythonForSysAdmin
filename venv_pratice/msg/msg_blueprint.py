from flask import Blueprint
import json

mensagens_routes = Blueprint(
    "mensagens",
    __name__,
    url_prefix="/mensagens"
)

@mensagens_routes.route("")
def getMensagens():
    return "Acessou mensagens"
