from bson.objectid import ObjectId
from flask import Blueprint, render_template, request, session, redirect, url_for
from flask.helpers import flash
from sqlalchemy import null
from validate_docbr import CPF

from app.models.plano import Plano
from ..models.aluno import Aluno

aluno = Blueprint('aluno', __name__, url_prefix="/aluno")

@aluno.route('/list')
def listAlunos():
    if "username" in session:
        alunos = Aluno.findAll()
        planos = Plano.findAll()
        return render_template("alunos/list.html", alunos = alunos , planos = planos)
    else:
        return redirect(url_for("usuario.index"))

@aluno.route('/plano')
def getPlano():
    aluno = Aluno.findByCPF(request.values.get("id"))
    return render_template("alunos/plano.html", plano=aluno.plano)

@aluno.route('/edit', methods=[ 'POST'])
def saveAluno():
        idAluno = request.form.get("idAluno") 
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")
        endereco = request.form.get("endereco")
        plano_id = request.form.get("plano")
        ativo = True if request.form.get("ativo") else False

        hasError = False
        validaCpf = CPF(repeated_digits = False)

        if not nome:
            flash("Campo 'nome' é obrigatório", "error")
            hasError = True
        if not validaCpf.validate(cpf):
            flash("Campo 'cpf' inválido", "error")
            hasError = True
        if not endereco:
            flash("Campo 'endereço' é obrigatório", "error")  
            hasError = True
        if not plano_id:
            flash("Campo 'plano' é obrigatório", "error")
            hasError = True
        
        alunoToSave = Aluno(nome = nome, cpf = cpf, endereco = endereco, plano_id = plano_id, ativo = ativo)
        if idAluno:
            alunoToSave.id = idAluno

        if hasError:
            alunos = Aluno.findAll()
            planos = Plano.findAll()
            return render_template("alunos/list.html", alunos=alunos, aluno=alunoToSave , planos = planos)

        alunoToSave.save()
        
        flash("Aluno salvo com sucesso", "info")
        return redirect(url_for("aluno.listAlunos"))

@aluno.route('/delete')
def deleteAluno():
    idAluno = request.values.get("idAluno")
    if not idAluno:
        flash("Campo 'idAluno' é obrigatório")
    else:
        alunoToDelete = Aluno.findById(idAluno)
        alunoToDelete.delete()
        flash("Aluno excluido com sucesso")
    return redirect(url_for("aluno.listAlunos"))
