# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from bson import ObjectId

from ..mongo_client_db import mongo_client_db
from ...utils import model2dict

collection = mongo_client_db.comments


class CommentCollection(object):
    def __init__(self):
        pass

    @staticmethod
    def get_comment_list():
        comment_list = collection.find({}, {"_id": 1, "title": 1})
        return comment_list

    @staticmethod
    def add_comment(comment):
        collection.insert(model2dict(comment))
