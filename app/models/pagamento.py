from sqlalchemy import Integer
from ..extentions.databaseMySQL import db
class Pagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpfAluno = db.Column(db.String(11), nullable=False)
    mesRef = db.Column(db.String(7), nullable=False)
    dataPagamento = db.Column(db.String(9), nullable=False)
    valorPago = db.Column(db.Numeric(2), nullable=False)
    tipo = db.Column(db.String(8), nullable=False)

    @classmethod
    def findAll(cls):
        return cls.query.all()

    @classmethod
    def findById(cls, idPagamento : Integer):
        return cls.query.filter_by(id = idPagamento).first()
        
    def save(self):
        if self.id:
            pagamentoToUpdate = self.findById(self.id)
            pagamentoToUpdate.cpfAluno = self.cpfAluno
            pagamentoToUpdate.mesRef = self.mesRef
            pagamentoToUpdate.dataPagamento = self.dataPagamento
            pagamentoToUpdate.valorPago = self.valorPago
            pagamentoToUpdate.tipo = self.tipo
        else:
            db.session.add(self)

        db.session.commit()
        return True
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True

    def __repr__(self):
        return '<Pagamento %s id %r valor %r>' %(self.cpfAluno, self.id, self.valorPago)
