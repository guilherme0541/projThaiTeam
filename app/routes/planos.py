from bson.objectid import ObjectId
from flask import Blueprint, render_template, request, session, redirect, url_for
from flask.helpers import flash

from app.models.modalidade import Modalidade
from ..models.plano import Plano

plano = Blueprint('plano', __name__, url_prefix="/plano")

@plano.route('/listPlanos')
def listPlanos():
    if "username" in session:
        planos = Plano.findAll()
        modalidades = Modalidade.findAll()    

        return render_template("planos/listPlano.html", planos=planos, modalidades = modalidades)
    else:
        return redirect(url_for("plano.index"))
   

@plano.route('Edit', methods=[ 'POST'])
def savePlano():
    idPlano = request.form.get("idPlano")
    descricao = request.form.get("descricao")
    valor = request.form.get("valor")
    descricaoModalidade = request.form.get("descModalidade")
    ativo = True if request.form.get("ativo") else False

    hasError = False
    if not descricao:
        flash("Campo 'descricao' é obrigatório", "error")
        hasError = True
    if not valor:
        flash("Campo 'valor' é obrigatório", "error")
        hasError = True
    if not descricaoModalidade:
        flash("Campo 'modalidade' é obrigatório", "error")
        hasError = True
    
    planoToSave = Plano(descricao = descricao, valor = valor, descricaoModalidade = descricaoModalidade, ativo = ativo)
    if idPlano:
        planoToSave.id = idPlano
    if hasError:
        planos = Plano.findAll()
        modalidades = Modalidade.findAll()   
        return render_template("planos/listPlano.html", planos=planos, plano=planoToSave, modalidades=modalidades)
    
    planoToSave.save()

    flash("Plano salvo com sucesso", "info")
    return redirect(url_for("plano.listPlanos"))

@plano.route('/delete')
def deletePlano():
    idPlano = request.values.get('idPlano')
    if not idPlano:
        flash("O campo 'idPlano' é obrigatório")
    else:
        try:
            planoToDelete = Plano.findById(idPlano)
            planoToDelete.delete()
            flash("Plano excluido com sucesso")
        except:
            flash("Não foi possível excluir plano. Um plano associado a um Aluno não pode ser excluído!")
    return redirect(url_for("plano.listPlanos"))


    