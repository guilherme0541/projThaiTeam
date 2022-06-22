from bson.objectid import ObjectId
from flask import Blueprint, render_template, request, session, redirect, url_for
from flask.helpers import flash

from app.models.instrutor import Instrutor

instrutor = Blueprint('instrutor', __name__)

@instrutor.route('/listInstrutores')
def listInstrutores():
    if "username" in session:
        instrutores = Instrutor.findAll()
        return render_template("instrutores/listInstrutores.html", instrutores=instrutores)
    else:
        return redirect(url_for("usuario.index"))

@instrutor.route('/insertInstrutores', methods=['GET', 'POST'])
def insertInstrutor():
    if request.method == 'GET':
        return render_template("Instrutores/insertInstrutores.html")
    else:
        nomeInstrutor = request.form.get('nomeInstrutor')
        enderecoInstrutor = request.form.get('enderecoInstrutor')
        contatoInstrutor = request.form.get('contatoInstrutor')
        dataAdmissao =  request.form.get('dataAdmissao')

        if not nomeInstrutor:
            flash("Campo 'Nome Instrutor' é obrigatório")
        elif not contatoInstrutor:
            flash("Campo 'Contato Instrutor' é obrigatório")
        elif not dataAdmissao:
            flash("Campo 'Data Admissao' é obrigatório")
        elif not enderecoInstrutor:
            flash("Campo 'enderecoInstrutor' é obrigatório")
        else:
            instrutorTOSave = Instrutor(nome = nomeInstrutor, endereco = enderecoInstrutor, contato = contatoInstrutor, dataAdmissao = dataAdmissao)
            instrutorTOSave.save()

            flash("Instrutor cadastrado com sucesso")
    return redirect(url_for("instrutor.listInstrutores"))

@instrutor.route('/editInstrutores', methods=['GET', 'POST'])
def editInstrutor():
    if request.method == "GET":
        idInstrutor = request.values.get("idInstrutor")

        if not idInstrutor:
            flash("Campo 'idInstrutor' é obrigatório")
            return redirect(url_for("instrutor.listInstrutores"))
        else:
            instrutor = Instrutor.findById(idInstrutor)         
            return render_template("Instrutores/editInstrutores.html", instrutor=instrutor)
    else:
        idInstrutor = request.form.get("idInstrutor")
        nomeInstrutor = request.form.get('nomeInstrutor')
        enderecoInstrutor = request.form.get('enderecoInstrutor')
        contatoInstrutor =  request.form.get('contatoInstrutor')
        dataAdmissao = request.form.get('dataAdmissao')

        if not idInstrutor:
            flash("Campo 'idInstrutor' é obrigatório")
        elif not nomeInstrutor:
            flash("Campo 'nomeInstrutor' é obrigatório")
        elif not enderecoInstrutor:
            flash("Campo 'enderecoInstrutor' é obrigatório")
        elif not contatoInstrutor:
            flash("Campo 'contatoInstrutor' é obrigatório")
        elif not dataAdmissao:
            flash("Campo 'dataAdmissao' é obrigatório")
        else:
            instrutorTOSave = Instrutor(id = idInstrutor, nome = nomeInstrutor, endereco = enderecoInstrutor, contato = contatoInstrutor, dataAdmissao = dataAdmissao)
            instrutorTOSave.save()

            flash("Instrutor alterado com sucesso")
        return redirect(url_for("instrutor.listInstrutores"))

@instrutor.route('/deleteInstrutores')
def deleteInstrutor():
    idInstrutor = request.values.get("idInstrutor")
    if not idInstrutor:
        flash("Campo 'idInstrutor' é obrigatório")
    else:
        instrutorToDelete = Instrutor.findById(idInstrutor)
        instrutorToDelete.delete()
        flash("Instrutor excluidaocom sucesso")
    return redirect(url_for("instrutor.listInstrutores"))