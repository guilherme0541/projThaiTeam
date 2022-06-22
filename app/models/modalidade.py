

from sqlalchemy import Integer
from ..extentions.databaseMySQL import db

class Modalidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    valorMensalidade = db.Column(db.Numeric(2), nullable=False)
    categoria = db.Column(db.String(20), nullable=False)

    @classmethod
    def findAll(cls):
        return cls.query.all()

    @classmethod
    def findById(cls, idModalidade : Integer):
        return cls.query.filter_by(id = idModalidade).first()
        
    def save(self):
        if self.id:
            modalidadeTOUpdate = self.findById(self.id)
            modalidadeTOUpdate.descricao = self.descricao
            modalidadeTOUpdate.valorMensalidade = self.valorMensalidade
            modalidadeTOUpdate.categoria = self.categoria
        else:
            db.session.add(self)

        db.session.commit()
        return True

    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True

    def __repr__(self):
        return '<Modalidade %s id %r valor %r>' %(self.descricao, self.id, self.valorMensalidade)
