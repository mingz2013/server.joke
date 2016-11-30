# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Blueprint, render_template

api = Blueprint('joke_controller', __name__, url_prefix='/joke')


@api.route('/', methods=['GET'])
def index():
    return render_template("home/joke/index.html")
