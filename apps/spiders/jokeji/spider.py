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
        self.get_search()

    def _create_site_client(self):
        return SiteClient(self._config)

    def get_search(self):

        for i in range(551):
            if i == 0:
                url = "http://www.jokeji.cn/list.htm"
            else:
                url = "http://www.jokeji.cn/list_%s.htm" % i
            response = self._site_client.get_search(url)
            self.parse_list(response)

        for i in range(526):
            url = "http://www.jokeji.cn/hot.asp?me_page=%s" % i
            response = self._site_client.get_search(url)
            self.parse_list_2(response)
        pass

    def parse_list(self, response):
        soup = BeautifulSoup(response.content, 'lxml')
        a_list = soup.select('div[class="list_title"] a')
        for a in a_list:
            href = a['href']
            url = "http://www.jokeji.cn" + href
            self.get_detail(url)
        pass

    def parse_list_2(self, response):
        soup = BeautifulSoup(response.content, 'lxml')
        a_list = soup.select('tr[valign="top"] a')
        for a in a_list:
            href = a['href']
            url = "http://www.jokeji.cn" + href
            self.get_detail(url)
        pass

    def get_detail(self, url):
        response = self._site_client.get_detail(url)
        soup = BeautifulSoup(response.content, 'lxml')
        p_list = soup.select('span[id="text110"] p')
        for p in p_list:
            result = p.getText()
