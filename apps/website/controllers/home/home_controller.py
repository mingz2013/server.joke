# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Blueprint, render_template

api = Blueprint('home_controller', __name__, url_prefix='')


@api.route('/', methods=['GET'])
def index():
    return render_template("home/index.html")


@api.route('/about', methods=['GET'])
def about():
    return render_template("home/about.html")


@api.route('/contact', methods=['GET'])
def contact():
    return render_template("home/contact.html")
