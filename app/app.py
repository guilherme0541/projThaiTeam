from flask import Flask

from .routes.aluno import aluno
from .routes.instrutor import instrutor
from .routes.modalidade import modalidade
from .routes.usuario import usuario
from .routes.pagamento import pagamento
from .routes.planos import plano
from .routes.relatorio import relatorio
from .routes.configuracao import configuracao

from .extentions import database
from .commands.userCommands import userCommands

def create_app(config_object = "app.settings"):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(aluno)
    app.register_blueprint(usuario)
    app.register_blueprint(modalidade)
    app.register_blueprint(instrutor)
    app.register_blueprint(pagamento)
    app.register_blueprint(plano)
    app.register_blueprint(relatorio)
    app.register_blueprint(configuracao)

    app.register_blueprint(userCommands)
    database.init_app(app)

    return app

