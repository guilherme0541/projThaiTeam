from bson.objectid import ObjectId
from flask import Blueprint, render_template, request, session, redirect, url_for
from flask.helpers import flash
from ..extentions.database import mongo

aluno = Blueprint('aluno', __name__)

@aluno.route('/home')
def listAlunos():
    return render_template("aluno/list.html")
