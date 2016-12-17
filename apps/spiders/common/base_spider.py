# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from base_site_client import BaseSiteClient


class BaseSpider(object):
    def __init__(self, config):
        self._config = config
        self._site_client = self._create_site_client()
        pass

    def run(self):
        raise NotImplementedError()

    def _create_site_client(self):
        return BaseSiteClient(self._config)
