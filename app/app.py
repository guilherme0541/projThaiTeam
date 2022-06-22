from flask import Flask

from .routes.aluno import aluno
from .routes.instrutor import instrutor
from .routes.modalidade import modalidade
from .routes.usuario import usuario
from .routes.pagamento import pagamento
from .routes.planos import plano
from .routes.relatorio import relatorio
from .routes.configuracao import configuracao

from .extentions import databaseMySQL
from .extentions.databaseMySQL import db
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
    databaseMySQL.init_app(app)

    @app.cli.command("createDB")
    def create_db():
        print("...apagando banco antigo...")
        db.drop_all()
        print("...criando banco...")
        db.create_all()
        print("...banco criado...")
        

    return app
