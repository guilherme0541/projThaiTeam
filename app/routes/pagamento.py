from datetime import datetime
from app.models.aluno import Aluno

from app.models.pagamentoDTO import PagamentoDTO
from ..models.pagamento import Pagamento
from bson.objectid import ObjectId
from flask import Blueprint, render_template, request, session, redirect, url_for
from flask.helpers import flash

pagamento = Blueprint('pagamento', __name__, url_prefix="/pagamento")

@pagamento.route('/list')
def listPagamentos():
    if "username" in session:
        pagamentos = Pagamento.findAll()

        for i in range(len(pagamentos)):
            pagamentos[i] = PagamentoDTO(pagamentos[i])

        print(pagamentos)
        alunos = Aluno.findAll()

        return render_template("pagamentos/list.html", pagamentos=pagamentos, alunos=alunos , mesRef=datetime.today().strftime('%m-%Y'), data=datetime.today().strftime('%d/%m/%Y'))
    else:
        return redirect(url_for("usuario.index"))

@pagamento.route('/edit', methods=[ 'POST'])
def savePagamento():
        idPagamento = request.form.get("idPagamento")
        cpfAluno = request.form.get("aluno")
        mesRef = request.form.get("mesRef")
        dataPagamento = request.form.get("dataPagamento")
        valorPago = request.form.get("valorPago")
        tipo = request.form.get("tipo")
        
        hasError = False

        if not cpfAluno:
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
        
        pagamentoToSave = Pagamento(cpfAluno = cpfAluno, mesRef = mesRef, dataPagamento = dataPagamento, valorPago = valorPago, tipo = tipo)
        
        if idPagamento:
            pagamentoToSave.id = idPagamento

        if hasError:
            pagamentos = Pagamento.findAll()

            for pagamento in pagamentos:
                pagamento = PagamentoDTO(pagamento)

            alunos = Aluno.findAll()
            return render_template("pagamentos/list.html", pagamentos=pagamentos , alunos=alunos , pagamento=PagamentoDTO(pagamentoToSave))

        pagamentoToSave.save()

        flash("Pagamento salvo com sucesso", "info")
        return redirect(url_for("pagamento.listPagamentos"))

@pagamento.route('/delete')
def deletePagamento():
    idPagamento = request.values.get("idPagamento")
    if not idPagamento:
        flash("Campo 'idPagamento' é obrigatório")
    else:
        pagamentoToDelete = Pagamento.findById(idPagamento)
        pagamentoToDelete.delete()
        flash("Pagamento excluido com sucesso")
    return redirect(url_for("pagamento.listPagamentos"))
