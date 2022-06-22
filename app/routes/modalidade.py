from bson.objectid import ObjectId
from flask import Blueprint, render_template, request, session, redirect, url_for
from flask.helpers import flash

from app.models.modalidade import Modalidade

modalidade = Blueprint('modalidade', __name__)

@modalidade.route('/list')
def listModalidades():
    if "username" in session:
        modalidades = Modalidade.findAll()
        return render_template("modalidades/list.html", modalidades=modalidades)
    else:
        return redirect(url_for("usuario.index"))

@modalidade.route('/insert', methods=['GET', 'POST'])
def insertModalidade():
    if request.method == 'GET':
        return render_template("modalidades/insert.html")
    else:
        descricao = request.form.get('descricao')
        categoria = request.form.get('categoria')
        valorMensalidade =  request.form.get('valorMensalidade')

        if not descricao:
            flash("Campo 'descricao' é obrigatório")
        elif not categoria:
            flash("Campo 'categoria' é obrigatório")
        elif not valorMensalidade:
            flash("Campo 'valorMensalidade' é obrigatório")
        else:
            modalidadeToSave = Modalidade(descricao = descricao, categoria = categoria, valorMensalidade = valorMensalidade)
            modalidadeToSave.save()

            flash("Categoria cadastrada com sucesso")
    return redirect(url_for("modalidade.listModalidades"))

@modalidade.route('/edit', methods=['GET', 'POST'])
def editModalidade():
    if request.method == "GET":
        idModalidade = request.values.get("idModalidade")

        if not idModalidade:
            flash("Campo 'idModalidade' é obrigatório")
            return redirect(url_for("modalidade.listModalidades"))
        else:
            modalidade =  Modalidade.findById(idModalidade)
            return render_template("modalidades/edit.html", modalidade=modalidade)
    else:
        idModalidade = request.form.get("idmodalidade")
        descricao = request.form.get('descricao')
        categoria = request.form.get('categoria')
        valorMensalidade =  request.form.get('valorMensalidade')

        if not idModalidade:
            flash("Campo 'idModalidade' é obrigatório")
        elif not descricao:
            flash("Campo 'descricao' é obrigatório")
        elif not valorMensalidade:
            flash("Campo 'valorMensalidade' é obrigatório")
        elif not categoria:
            flash("Campo 'categoria' é obrigatório")
        else:
            modalidadeToSave = Modalidade(id = idModalidade, descricao = descricao, categoria = categoria, valorMensalidade = valorMensalidade)
            modalidadeToSave.save()
            
            flash("Modalidade alterada com sucesso")
        return redirect(url_for("modalidade.listModalidades"))

@modalidade.route('/delete')
def deleteModalidade():
    idModalidade = request.values.get("idModalidade")
    if not idModalidade:
        flash("Campo 'idModalidade' é obrigatório")
    else:
        modalidadeToDelete = Modalidade.findById(idModalidade)
        modalidadeToDelete.delete()
        flash("Modalidade excluida com sucesso")
    return redirect(url_for("modalidade.listModalidades"))