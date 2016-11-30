# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

from bs4 import BeautifulSoup

from commons.spider.exception import Error302, Error403
from site_client import SiteClient


class Spider(object):
    def __init__(self):
        self._client = SiteClient(proxies={})
        pass

    def run(self):
        pass
