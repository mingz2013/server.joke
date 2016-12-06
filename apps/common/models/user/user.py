# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time

from ..base0 import Base0
from ...utils.utils import require_value_from_dict


class User(Base0):
    """
    用户
    """

    def __init__(self, obj):
        Base0.__init__(self)

        self.username = require_value_from_dict(obj, 'username')
        self.password = require_value_from_dict(obj, 'password')

        self.email = require_value_from_dict(obj, 'email')
        self.mobile = require_value_from_dict(obj, 'mobile')
        self.sex = require_value_from_dict(obj, 'sex')

        self.create_time = time.time()
        self.update_time = time.time()

        self.permission = require_value_from_dict(obj, 'permission')  # admin, author

        self.status = 0  # 0: 正常, -1: 删除
