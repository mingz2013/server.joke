# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Blueprint, render_template

api = Blueprint('init_controller', __name__, url_prefix='/init')


@api.route('/', methods=['GET'])
def index():
    return render_template("init/index.html")
