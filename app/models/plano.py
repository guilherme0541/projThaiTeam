from sqlalchemy import Integer
from ..extentions.databaseMySQL import db

class Plano(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Numeric(2), nullable=False)
    descricaoModalidade = db.Column(db.String(100), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)

    @classmethod
    def findAll(cls):
        return cls.query.all()

    @classmethod
    def findById(cls, idPlano : Integer):
        return cls.query.filter_by(id = idPlano).first()
        
    def save(self):
        if self.id:
            planoTOUpdate = self.findById(self.id)
            planoTOUpdate.descricao = self.descricao
            planoTOUpdate.valor = self.valor
            planoTOUpdate.descricaoModalidade = self.descricaoModalidade
            planoTOUpdate.ativo = self.ativo
        else:
            db.session.add(self)

        db.session.commit()
        return True
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True

    def __repr__(self):
        return '<Plano %s id %r valor %r>' %(self.descricao, self.id, self.valor)
