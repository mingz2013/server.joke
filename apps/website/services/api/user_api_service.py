# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from commons.mongo_db.user.user_db import UserDB
from commons.utils.utils import model2dict


class UserAPIService(object):
    def __init__(self):
        pass

    @staticmethod
    def login(user):
        UserDB.check_login(user)
        pass

    @staticmethod
    def get_user_list():
        user_list = UserDB.get_user_list()
        user_list_copy = []
        for user in user_list:
            user_list_copy.append({
                "_id": str(user.get('_id')),
                "username": user.get('username'),
                "permission": user.get('permission')
            })
        return user_list_copy

    @staticmethod
    def get_user_detail(user_id):
        user = UserDB.get_user_by_id(user_id)
        user_copy = {}
        user_copy.update({
            "_id": str(user.get('_id')),
            "username": user.get('username'),
            "email": user.get('email'),
            "mobile": user.get('mobile'),
            "sex": user.get("sex"),
            "permission": user.get("permission"),
            "create_time": user.get("create_time")
        })
        return user_copy

    @staticmethod
    def remove_user(user_id):
        UserDB.remove_user_by_id(user_id)

    @staticmethod
    def add_user(user):
        return UserDB.add_user(user)

    @staticmethod
    def update_user(user_id, user):
        UserDB.update_user(user_id, user)
