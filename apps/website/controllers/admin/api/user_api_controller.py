# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import request, Blueprint, jsonify, current_app

from ....services.api.user_api_service import UserAPIService
from commons.models.user.user import User

api = Blueprint('user_api_controller', __name__, url_prefix='/api/user')


@api.route('/', methods=['GET'])
def index():
    return "user index"


@api.route('/', methods=['POST'])
def login():
    try:
        user = User(request.form)
        result = UserAPIService.login(user)
        return jsonify({'retcode': 0, 'errmsg': "", 'result': result})
    except Exception, e:
        return jsonify({'retcode': -1, 'errmsg': e.message, 'result': ""})


@api.route('/list', methods=['GET'])
def list():
    try:
        user_list = UserAPIService.get_user_list()
        return jsonify({'retcode': 0, 'errmsg': "", 'result': user_list})
    except Exception, e:
        return jsonify({'retcode': -1, 'errmsg': e.message, 'result': ""})


@api.route('/detail/<user_id>', methods=['GET'])
def detail(user_id):
    try:
        user = UserAPIService.get_user_detail(user_id)
        return jsonify({'retcode': 0, 'errmsg': "", 'result': user})
    except Exception, e:
        return jsonify({'retcode': -1, 'errmsg': e.message, 'result': ""})


@api.route('/add', methods=['POST'])
def add():
    try:
        user = User(request.form)
        user_id = UserAPIService.add_user(user)
        return jsonify({'retcode': 0, 'errmsg': "", 'result': str(user_id)})
    except Exception, e:
        return jsonify({'retcode': -1, 'errmsg': e.message, 'result': ""})


@api.route('/remove/<user_id>', methods=['DELETE'])
def remove(user_id):
    try:
        UserAPIService.remove_user(user_id)
        return jsonify({'retcode': 0, 'errmsg': "", 'result': "success"})
    except Exception, e:
        return jsonify({'retcode': -1, 'errmsg': e.message, 'result': ""})


@api.route('/update', methods=['PUT'])
def update():
    user = User(request.form)
    user_id = str(request.form['_id'])
    current_app.logger.info(user)
    current_app.logger.info(user_id)
    try:
        UserAPIService.update_user(user_id, user)
        return jsonify({'retcode': 0, 'errmsg': "", 'result': "success"})
    except Exception, e:
        return jsonify({'retcode': -1, 'errmsg': e.message, 'result': ""})
