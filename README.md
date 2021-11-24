# projThaiTeam
Sistema de gerenciamento de alunos e mensalidades desenvolvido para o Centro de treinamento Thai Team no Projeto Integrador na Univesp.



Para executar este projeto, após criar e ativar seu ambiente virtual, instale as dependências (estando na raiz do projeto) com :

```
pip install -r requirements.txt
```

Crie um arquivo .env assim:

```
FLASK_APP=app/app.py
FLASK_ENV=development
MONGO_URI="<String Connection mongo>/<database>"
SECRET_KEY="secret key"
```

Crie um usuário com:

```
Flask user addUser nomeDoUsuario
```

e obedeça o terminal =] 


Agora você está pronto para:

```
flask run
```

O App está acessível em localhost:5000
