# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Blueprint, jsonify, request

from ....services.api.category_api_service import CategoryAPIService
from commons.models.article.category import Category

api = Blueprint('category_api_controller', __name__, url_prefix='/api/category')


@api.route('/', methods=['GET'])
def index():
    return 'article index'


@api.route('/list', methods=['GET'])
def list():
    try:
        category_list = CategoryAPIService.get_category_list()
        return jsonify({'retcode': 0, 'errmsg': "", 'result': category_list})
    except Exception, e:
        return jsonify({'retcode': -1, 'errmsg': e.message, 'result': ""})


@api.route('/add', methods=['POST'])
def add():
    try:
        category = Category(request.form['title'])
        CategoryAPIService.add_category(category)
        return jsonify({'retcode': 0, 'errmsg': "", 'result': "success"})
    except Exception, e:
        return jsonify({'retcode': -1, 'errmsg': e.message, 'result': ""})

#

# @api.route('/detail/<article_id>', methods=['GET'])
# def detail(article_id):
#     try:
#         article = ArticleAPIService.get_article_detail(article_id)
#         return jsonify({'retcode': 0, 'errmsg': "", 'result': article})
#     except Exception, e:
#         return jsonify({'retcode': -1, 'errmsg': e.message, 'result': ""})
#
#

# @api.route('/remove/<article_id>', methods=['DELETE'])
# def remove(article_id):
#     try:
#         ArticleAPIService.remove_article(article_id)
#         return jsonify({'retcode': 0, 'errmsg': "", 'result': 'success'})
#     except Exception, e:
#         return jsonify({'retcode': -1, 'errmsg': e.message, 'result': ""})
#
#
# @api.route('/update', methods=['PUT'])
# def update():
#     try:
#         article = request.form['article']
#         ArticleAPIService.update_article(article)
#         return jsonify({'retcode': 0, 'errmsg': "", 'result': "success"})
#     except Exception, e:
#         return jsonify({'retcode': -1, 'errmsg': e.message, 'result': ""})
