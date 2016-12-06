# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from bson import ObjectId

from ..mongo_client_db import mongo_client_db
from ...utils.utils import model2dict


class CategoryDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_category_list():
        category_list = mongo_client_db.categories.find({}, {"_id": 1, "title": 1})
        return category_list

    @staticmethod
    def add_category(category):
        mongo_client_db.categories.insert(model2dict(category))
