from datetime import datetime
from ..models.pagamento import Pagamento
from bson.objectid import ObjectId
from flask import Blueprint, render_template, request, session, redirect, url_for
from flask.helpers import flash
from ..extentions.database import mongo

pagamento = Blueprint('pagamento', __name__, url_prefix="/pagamento")

@pagamento.route('/list')
def listPagamentos():
    if "username" in session:
        pagamentos = mongo.db.pagamentos.find()
        alunos = mongo.db.alunos.find()
        return render_template("pagamentos/list.html", pagamentos=pagamentos, alunos=alunos , mesRef=datetime.today().strftime('%m-%Y'), data=datetime.today().strftime('%d-%m-%Y'))
    else:
        return redirect(url_for("usuario.index"))

@pagamento.route('/edit', methods=[ 'POST'])
def savePagamento():
        idPagamento = request.form.get("idPagamento")
        aluno = mongo.db.alunos.find_one({"_id": ObjectId(request.form.get("aluno"))})
        mesRef = request.form.get("mesRef")
        dataPagamento = request.form.get("dataPagamento")
        valorPago = request.form.get("valorPago")
        tipo = request.form.get("tipo")
        
        hasError = False

        if not aluno:
            flash("Campo 'aluno' é obrigatório", "error")
            hasError = True
        if not mesRef:
            flash("Campo 'Mês de Referência' é obrigatório", "error")
            hasError = True
        if not dataPagamento:
            flash("Campo 'Data do Pagamento' é obrigatório", "error")  
            hasError = True
        if not valorPago:
            flash("Campo 'Valor Pago' é obrigatório", "error")
            hasError = True
        
        if hasError:
            pagamentoToSave = Pagamento(idPagamento,  aluno, mesRef, dataPagamento, valorPago, tipo)
            pagamentos = mongo.db.pagamentos.find()
            alunos = mongo.db.alunos.find()
            return render_template("pagamentos/list.html", pagamentos=pagamentos , alunos=alunos , pagamento=pagamentoToSave)

        if not idPagamento:
             mongo.db.pagamentos.insert_one({
                "aluno": aluno,
                "mesRef": mesRef,
                "dataPagamento": dataPagamento,
                "valorPago" : valorPago,
                "tipo" : tipo
            })
        else:
            mongo.db.pagamentos.update({"_id": ObjectId(idPagamento)},
            {
                "$set":{
                    "aluno": aluno,
                    "mesRef": mesRef,
                    "dataPagamento": dataPagamento,
                    "valorPago" : valorPago,
                    "tipo" : tipo
                }
            })
        flash("Pagamento salvo com sucesso", "info")
        return redirect(url_for("pagamento.listPagamentos"))

@pagamento.route('/delete')
def deletePagamento():
    idPagamento = request.values.get("idPagamento")
    if not idPagamento:
        flash("Campo 'idPagamento' é obrigatório")
    else:
        mongo.db.pagamentos.delete_one({"_id": ObjectId(idPagamento)})
        flash("Pagamento excluido com sucesso")
    return redirect(url_for("pagamento.listPagamentos"))
