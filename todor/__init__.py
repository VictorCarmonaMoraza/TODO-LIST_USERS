from logging import DEBUG
from . import todo, auth

from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    ##Configuracion del proyecto
    app.config.from_mapping(
        DEBUG=True,
        SECRET_KEY='dev',
    )

    #Registro de blueprints
    app.register_blueprint(todo.bp)
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return  render_template('index.html')

    return app