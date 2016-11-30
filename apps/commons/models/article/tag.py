# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time

from ..base0 import Base0
from ...utils.utils import require_value_from_dict


class Tag(Base0):
    """
    文章标签
    """

    def __init__(self, title):
        Base0.__init__(self)

        self.title = title
        self.status = 0  # 0: 正常, -1: 删除
        self.article_count = 0
        self.create_time = time.time()
        self.update_time = time.time()
        pass
