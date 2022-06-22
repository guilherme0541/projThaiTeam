from app.models.aluno import Aluno
from app.models.pagamento import Pagamento


class PagamentoDTO():
    def __init__(self, pagamento : Pagamento):
        self.id = pagamento.id
        self.aluno = Aluno.findByCPF(pagamento.cpfAluno)
        self.mesRef = pagamento.mesRef
        self.dataPagamento = pagamento.dataPagamento
        self.valorPago = pagamento.valorPago
        self.tipo = pagamento.tipo

    def __repr__(self):
        return '<Pagamento %s id %r valor %r>' %(self.aluno, self.id, self.valorPago)
