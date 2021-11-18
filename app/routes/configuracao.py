from bson.objectid import ObjectId
from flask import Blueprint, render_template, request, session, redirect, url_for
from flask.helpers import flash
from ..extentions.database import mongo

configuracao = Blueprint('configuracao', __name__)

@configuracao.route('/home')
def listConfiguracoes():
    return render_template("configuracao/list.html")