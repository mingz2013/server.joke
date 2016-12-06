# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time

from ..base0 import Base0
from ...utils import require_value_from_dict


class Site(Base0):
    """
    来源
    """
    def __init__(self, obj):
        Base0.__init__(self)

        self.domain = require_value_from_dict(obj, 'domain')
        self.name = require_value_from_dict(obj, 'name')
        self.date = time.time()
        self.status = 0  # -1: 删除, 0: 草稿, 1:发布
