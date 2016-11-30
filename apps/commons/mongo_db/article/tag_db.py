# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from bson import ObjectId

from ..mongo_client_db import mongo_client_db
from ...utils.utils import model2dict


class TagDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_tag_list():
        tag_list = mongo_client_db.tags.find({}, {"_id": 1, "title": 1})
        return tag_list

    @staticmethod
    def add_tag(tag):
        mongo_client_db.tags.insert(model2dict(tag))
