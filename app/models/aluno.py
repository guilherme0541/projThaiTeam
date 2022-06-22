from enum import unique
from sqlalchemy import Integer, true
from ..extentions.databaseMySQL import db
class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    endereco = db.Column(db.String(100), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)

    plano_id = db.Column(db.Integer, db.ForeignKey('plano.id'), nullable=False)
    plano = db.relationship('Plano', backref=db.backref('alunos', lazy=True))

    @classmethod
    def findAll(cls):
        return cls.query.all()

    @classmethod
    def findById(cls, idAluno : Integer):
        return cls.query.filter_by(id =idAluno).first()

    @classmethod
    def findByCPF(cls, cpfAluno : Integer):
        return cls.query.filter_by(cpf = cpfAluno).first()
        
    def save(self):
        if self.id:
            alunoToUpdate = self.findById(self.id)
            alunoToUpdate.nome = self.nome
            alunoToUpdate.cpf = self.cpf
            alunoToUpdate.endereco = self.endereco
            alunoToUpdate.ativo = self.ativo
            alunoToUpdate.plano_id = self.plano_id
        else:
            db.session.add(self)

        db.session.commit()
        return True

    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return true

    def __repr__(self):
        return '<Aluno %s id %r plano %r>' %(self.nome, self.id, self.plano)