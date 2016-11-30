# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from website.services.tools.init_tool_service import InitToolService


def init_dbs():
    InitToolService.init_dbs()
    pass


if __name__ == "__main__":
    init_dbs()
    pass
