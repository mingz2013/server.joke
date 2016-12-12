# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from bson import ObjectId

from ..mongo_client_db import mongo_client_db
from ...utils import model2dict

collection = mongo_client_db.jokes


class JokeCollection(object):
    def __init__(self):
        pass

    @staticmethod
    def get_joke_list():
        joke_list = collection.find()
        return joke_list
