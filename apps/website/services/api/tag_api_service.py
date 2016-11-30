# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from commons.mongo_db.article.tag_db import TagDB


class TagAPIService(object):
    def __init__(self):
        pass

    @staticmethod
    def get_tag_list():
        tag_list = TagDB.get_tag_list()
        i = 0
        tag_list_copy = []
        for tag in tag_list:
            tag_copy = {}
            tag_copy.update(tag)
            tag_copy.update({
                "_id": str(tag.get('_id')),
                "title": tag.get("title"),
            })
            tag_list_copy.append(tag_copy)
            i += 1

        return tag_list_copy

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
    def add_tag(tag):
        TagDB.add_tag(tag)
        #
        # @staticmethod
        # def update_article(article):
        #     ArticleDB.update_article(article)
