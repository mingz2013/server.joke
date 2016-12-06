# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from bson import ObjectId

from ..mongo_client_db import mongo_client_db
from ...utils import model2dict

collection = mongo_client_db.tags


class TagCollection(object):
    def __init__(self):
        pass

    @staticmethod
    def get_tag_list():
        tag_list = collection.find({}, {"_id": 1, "title": 1})
        return tag_list

    @staticmethod
    def add_tag(tag):
        collection.insert(model2dict(tag))
