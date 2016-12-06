# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from base_site_client import BaseSiteClient


class BaseSpider(object):
    def __init__(self, config):
        self._config = config
        self._create_site_client()
        pass

    def run(self):
        pass

    def _create_site_client(self):
        self._site_client = BaseSiteClient(self._config)
        pass
