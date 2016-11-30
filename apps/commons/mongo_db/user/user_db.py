# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from bson import ObjectId

from ..mongo_client_db import mongo_client_db
from ...utils.utils import model2dict


class UserDB(object):
    def __init__(self):
        pass

    @staticmethod
    def check_login(user):
        user = mongo_client_db.users.find_one(user)
        if user:
            return True
        else:
            return False

    @staticmethod
    def remove_all_users():
        mongo_client_db.users.drop()

    @staticmethod
    def add_user(user):
        user_id = mongo_client_db.users.insert(model2dict(user))
        return user_id

    @staticmethod
    def get_user_list():
        users = mongo_client_db.users.find({}, {"_id": 1, "permission": 1, "username": 1})
        return users

    @staticmethod
    def get_user_by_id(user_id):
        user = mongo_client_db.users.find_one({"_id": ObjectId(user_id)},
                                              {"username": 1, "email": 1, "mobile": 1, "sex": 1, "create_time": 1,
                                               "update_time": 1, "permission": 1})
        return user

    @staticmethod
    def remove_user_by_id(user_id):
        mongo_client_db.users.remove({"_id": ObjectId(user_id)})

    @staticmethod
    def update_user(user_id, user):
        mongo_client_db.users.update({"_id": ObjectId(user_id)}, model2dict(user))

    @staticmethod
    def get_admin_user():
        admin = mongo_client_db.users.find_one({"permission": "admin"}, {"_id": 1})
        if admin:
            return True
        else:
            return False

    @staticmethod
    def get_author_info_by_id(user_id):
        user = mongo_client_db.users.find_one({"_id": ObjectId(user_id)}, {"username": 1, "permission": 1})
        return user
