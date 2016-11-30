# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from commons.mongo_db.article.category_db import CategoryDB


class CategoryAPIService(object):
    def __init__(self):
        pass

    @staticmethod
    def get_category_list():
        category_list = CategoryDB.get_category_list()
        i = 0
        category_list_copy = []
        for category in category_list:
            category_copy = {}
            category_copy.update({
                "_id": str(category.get('_id')),
                "title": category.get("title"),
            })
            category_list_copy.append(category_copy)
            i += 1
        # print category_list_copy
        return category_list_copy

        # @staticmethod
        # def get_article_detail(article_id):
        #     article = ArticleDB.get_article_by_id(article_id)
        #     article_copy = {}
        #     article_copy.update(article)
        #     article_copy.update({
        #         "author": UserDB.get_author_info_by_id(article['user_id'])
        #     })
        #     return article_copy
        #
        # @staticmethod
        # def remove_article(article_id):
        #     ArticleDB.remove_article_by_id(article_id)
        #

    @staticmethod
    def add_category(category):
        CategoryDB.add_category(category)
        #
        # @staticmethod
        # def update_article(article):
        #     ArticleDB.update_article(article)
