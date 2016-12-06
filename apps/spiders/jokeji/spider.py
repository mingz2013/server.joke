# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

from bs4 import BeautifulSoup

from apps.spiders.common.exception import Error302, Error403, Error404, Error502, Error503, ErrorStatusCode, \
    HttpClientError, \
    MoreCheckverifyCodeTimesError, NeedrefreshProxyError, NeedrefreshSearchKeyError

from site_client import SiteClient
from ..common.base_spider import BaseSpider


class Spider(BaseSpider):
    def __init__(self, config):
        BaseSpider.__init__(self, config)

        pass

    def run(self):
        pass
