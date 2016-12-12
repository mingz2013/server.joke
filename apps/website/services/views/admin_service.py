# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from apps.common.mongo_db.user.user_collection import UserCollection


class AdminService(object):
    def __init__(self):
        pass

    @staticmethod
    def check_is_need_init():
        if UserCollection.get_admin_user():
            return False
        else:
            return True

    @staticmethod
    def check_is_login():
        return True
