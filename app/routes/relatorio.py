from bson.objectid import ObjectId
from flask import Blueprint, render_template, request, session, redirect, url_for
from flask.helpers import flash

relatorio = Blueprint('relatorio', __name__)

@relatorio.route('/homeRelatorio')
def listRelatorios():
    return render_template("relatorio/list.html")