import click
import getpass
from werkzeug.security import generate_password_hash
from flask import Blueprint, cli
from app.models.user import User

userCommands = Blueprint('user', __name__)

@userCommands.cli.command("getUser")
@click.argument("name")
def get_user(name):
    user = User.findByName(name)

@userCommands.cli.command("addUser")
@click.argument("name")
def create_user(name):
    if User.findByName(name):
        print(f'Usuário {name} já existe')
    else:
        senha = getpass.getpass()
        user = User(name = name, password = generate_password_hash(senha))
        user.save()
        print('Usuário cadastrado com sucesso')

@userCommands.cli.command("deleteUser")
@click.argument("name")
def delete_user(name):
    user = User.findByName(name)
    if user:
        question = input(f'Deseja realmente deletar o usuário {name}? (S/N)')

        if question.upper() == "S":
            user.delete()
            print("Usuário deletado com sucesso!")
        else:
            exit()
    else:
        print("Usuário não encontrado")


