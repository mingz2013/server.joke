# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging
import math
import time
import urllib2
from bs4 import BeautifulSoup

from ..common.base_site_client import BaseSiteClient


class SiteClient(BaseSiteClient):
    def __init__(self, config, proxies={}):
        BaseSiteClient.__init__(config, proxies)
        pass
