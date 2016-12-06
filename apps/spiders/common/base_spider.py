# -*- coding:utf-8 -*-
__author__ = 'zhaojm'


class BaseSpider(object):
    def __init__(self, config):
        self._config = config
        pass

    def run(self):
        pass
