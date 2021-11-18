from bson.objectid import ObjectId
from flask import Blueprint, render_template, request, session, redirect, url_for
from flask.helpers import flash
from ..extentions.database import mongo
from ..models.aluno import Aluno

aluno = Blueprint('aluno', __name__, url_prefix="/aluno")

@aluno.route('/list')
def listAlunos():
    if "username" in session:
        alunos = mongo.db.alunos.find()
        return render_template("alunos/list.html", alunos=alunos)
    else:
        return redirect(url_for("usuario.index"))

@aluno.route('/edit', methods=[ 'POST'])
def saveAluno():
        idAluno = request.form.get("idAluno")
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")
        endereco = request.form.get("endereco")
        plano = request.form.get("plano")
        ativo = request.form.get("ativo")
        hasError = False

        if not nome:
            flash("Campo 'nome' é obrigatório", "error")
            hasError = True
        if not cpf:
            flash("Campo 'cpf' é obrigatório", "error")
            hasError = True
        if not endereco:
            flash("Campo 'endereço' é obrigatório", "error")  
            hasError = True
        if not plano:
            flash("Campo 'plano' é obrigatório", "error")
            hasError = True
        
        if hasError:
            alunoToSave = Aluno(idAluno,  nome, cpf, endereco, plano, ativo)
            alunos = mongo.db.alunos.find()
            return render_template("alunos/list.html", alunos=alunos, aluno=alunoToSave)

        if not idAluno:
             mongo.db.alunos.insert_one({
                "nome": nome,
                "cpf": cpf,
                "endereco": endereco,
                "plano" : plano,
                "ativo" : ativo
            })
        else:
            mongo.db.alunos.update({"_id": ObjectId(idAluno)},
            {
                "$set":{
                    "nome": nome,
                    "cpf": cpf,
                    "endereco": endereco,
                    "plano" : plano,
                    "ativo" : ativo
                }
            })
        flash("Aluno salvo com sucesso", "info")
        return redirect(url_for("aluno.listAlunos"))

@aluno.route('/delete')
def deleteAluno():
    idAluno = request.values.get("idAluno")
    if not idAluno:
        flash("Campo 'idAluno' é obrigatório")
    else:
        mongo.db.alunos.delete_one({"_id": ObjectId(idAluno)})
        flash("Aluno excluido com sucesso")
    return redirect(url_for("aluno.listAlunos"))
