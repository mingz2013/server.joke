# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from bson import ObjectId

from ..mongo_client_db import mongo_client_db
from ...utils import model2dict

collection = mongo_client_db.categories


class CategoryCollection(object):
    def __init__(self):
        pass

    @staticmethod
    def get_category_list():
        category_list = collection.find({}, {"_id": 1, "title": 1})
        return category_list

    @staticmethod
    def add_category(category):
        collection.insert(model2dict(category))
