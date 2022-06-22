
from sqlalchemy import Integer, true
from ..extentions.databaseMySQL import db

class Instrutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(100), nullable=False)
    contato = db.Column(db.String(100), nullable=False)
    dataAdmissao = db.Column(db.String(9), nullable=False)

    @classmethod
    def findAll(cls):
        return cls.query.all()

    @classmethod
    def findById(cls, idInstrutor : Integer):
        return cls.query.filter_by(id =idInstrutor).first()
        
    def save(self):
        if self.id:
            instrutorToUpdate = self.findById(self.id)
            instrutorToUpdate.nome = self.nome
            instrutorToUpdate.endereco = self.endereco
            instrutorToUpdate.contato = self.contato
            instrutorToUpdate.dataAdmissao = self.dataAdmissao
        else:
            db.session.add(self)

        db.session.commit()
        return True

    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return true

    def __repr__(self):
        return '<Instrutor %s id %r dataAdmissao %r>' %(self.nome, self.id, self.dataAdmissao)