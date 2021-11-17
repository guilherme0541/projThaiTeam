from flask import Flask
from .routes.aluno import aluno
from .routes.usuario import usuario
from .routes.modalidade import modalidade
from .extentions import database
from .commands.userCommands import userCommands

def create_app(config_object = "app.settings"):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(usuario)
    app.register_blueprint(modalidade , url_prefix='/modalidade')
    app.register_blueprint(aluno, url_prefix='/aluno')

    app.register_blueprint(userCommands)
    database.init_app(app)

    return app

