from bson.objectid import ObjectId
from flask import Blueprint, render_template, request, session, redirect, url_for
from flask.helpers import flash
from ..extentions.database import mongo

plano = Blueprint('plano', __name__)

@plano.route('/home')
def listPlanos():
    return render_template("planos/list.html")