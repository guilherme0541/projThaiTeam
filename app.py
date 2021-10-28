import os

from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#BD config

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "db/database.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Aluno(db.Model):
    idAluno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return  '<Aluno %r , id: %r>' % self.name, self.idAluno



#Routes
@app.route("/")
def home():
    return "Hello world!"

@app.route("/alunos", methods=["GET", "POST"])
def criarAluno():
    if request.form:
        aluno = Aluno(idAluno=request.form.get("idAluno"), name=request.form.get("name"))
        db.session.add(aluno)
        db.session.commit()
    alunos = Aluno.query.all()
    return render_template("form.html", alunos=alunos)
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
