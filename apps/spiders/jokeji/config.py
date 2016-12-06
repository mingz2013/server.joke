# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from apps.spiders.common.base_config import BaseConfig


class Config(BaseConfig):
    def __init__(self):
        BaseConfig.__init__(self)

    def _get_host(self):
        return "www.jokeji.cn"
