# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time

from ..base0 import Base0
from ...utils import require_value_from_dict


class Comment(Base0):
    """
    评论
    """

    def __init__(self, obj):
        Base0.__init__(self)

        self.title = require_value_from_dict(obj, 'title')
        self.content = require_value_from_dict(obj, 'content')
        self.author = require_value_from_dict(obj, 'author')

        self.status = 0  # 0: 正常, -1: 删除

        self.date = time.time()
        self.modified = time.time()
        pass
