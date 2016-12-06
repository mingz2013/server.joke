# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time

from ..base0 import Base0


class Tag(Base0):
    """
    标签
    """

    def __init__(self, title):
        Base0.__init__(self)

        self.title = title
        self.status = 0  # 0: 正常, -1: 删除
        self.date = time.time()
        self.modified = time.time()
        pass
