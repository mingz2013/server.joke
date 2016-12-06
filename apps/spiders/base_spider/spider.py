# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

from bs4 import BeautifulSoup

from site_client import SiteClient

from ..common.base_spider import BaseSpider


class Spider(BaseSpider):
    def __init__(self, config):
        BaseSpider.__init__(self, config)
        pass

    def run(self):
        pass

    def _create_site_client(self):
        return SiteClient(self._config)
