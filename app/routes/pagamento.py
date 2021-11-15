from bson.objectid import ObjectId
from flask import Blueprint, render_template, request, session, redirect, url_for
from flask.helpers import flash
from ..extentions.database import mongo

pagamento = Blueprint('pagamento', __name__)

@pagamento.route('/home')
def listPagamentos():
    return render_template("pagamentos/list.html")