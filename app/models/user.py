from typing_extensions import Self
from unicodedata import name
from sqlalchemy import Integer
from ..extentions.databaseMySQL import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    @classmethod
    def findAll(cls):
        return cls.query.all()

    @classmethod
    def findByName(cls, userName: Integer)->Self:
        return cls.query.filter_by(name = userName).first()
                
    def save(self):
        db.session.add(self)
        db.session.commit()
        return True

    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True