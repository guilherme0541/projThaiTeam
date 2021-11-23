from bson.objectid import ObjectId
from flask import Blueprint, render_template, request, session, redirect, url_for
from flask.helpers import flash
from ..extentions.database import mongo
from ..models.plano import Plano

plano = Blueprint('plano', __name__, url_prefix="/plano")

@plano.route('/listPlanos')
def listPlanos():
    if "username" in session:
        planos = mongo.db.planos.find()
        modalidades = mongo.db.modalidades.find()       

        return render_template("planos/listPlano.html", planos=planos, modalidades = modalidades)
    else:
        return redirect(url_for("plano.index"))
   

@plano.route('Edit', methods=[ 'POST'])
def savePlano():
    idPlano = request.form.get("idPlano")
    descricao = request.form.get("descricao")
    valor = request.form.get("valor")
    descricaoModalidade = request.form.get("descModalidade")
    ativo = request.form.get("ativo")

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
    
    if hasError:
        planoToSave = Plano(idPlano, descricao, valor, descricaoModalidade, ativo)
        planos = mongo.db.planos.find()
        modalidades = mongo.db.modalidades.find()
        return render_template("planos/listPlano.html", planos=planos, plano=planoToSave, modalidades=modalidades)
    
    if not idPlano:
        mongo.db.planos.insert_one({
            "descricao": descricao,
            "valor": valor,
            "descricaoModalidade": descricaoModalidade,
            "ativo": ativo
        })
    else:
        mongo.db.planos.update({"_id": ObjectId(idPlano)},{
            "$set":{
                "descricao": descricao,
                "valor": valor,
                "descricaoModalidade": descricaoModalidade,
                "ativo": ativo
            }
        })
    flash("Plano salvo com sucesso", "info")
    return redirect(url_for("plano.listPlanos"))

@plano.route('/delete')
def deletePlano():
    idPlano = request.values.get('idPlano')
    if not idPlano:
        flash("O campo 'idPlano' é obrigatório")
    else:
        mongo.db.planos.delete_one({"_id": ObjectId(idPlano)})
        flash("Plano excluido com sucesso")
    return redirect(url_for("plano.listPlanos"))


    