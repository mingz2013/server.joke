# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time

from ..base0 import Base0
from ...utils import require_value_from_dict, get_value_from_dict


class Joke(Base0):
    """
    笑话
    """

    def __init__(self, obj):
        Base0.__init__(self)

        self.title = get_value_from_dict(obj, 'title')
        self.content = require_value_from_dict(obj, 'content')

        self.author = get_value_from_dict(obj, 'author')

        self.from_site = get_value_from_dict(obj, 'from_site')

        self.category = get_value_from_dict(obj, 'category')
        self.tags = get_value_from_dict(obj, 'tags')

        self.date = time.time()
        self.modified = time.time()

        self.status = 0  # -1: 删除, 0: 草稿, 1:发布

        self.view_times = 0
