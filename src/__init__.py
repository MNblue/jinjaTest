from flask import Flask, request, jsonify, json;

#registrar rutas
from .routes import clienteRoutes
from .routes import process



app= Flask(__name__)


def init_app(config):
    app.config.from_object(config)
    app.register_blueprint(clienteRoutes.main, url_prefix='/')

    app.register_blueprint(clienteRoutes.main2, url_prefix='/procesar')
    
    return app
