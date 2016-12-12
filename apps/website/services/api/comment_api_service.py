# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from apps.common.mongo_db.joke.comment_collection import CommentCollection


class CommentAPIService(object):
    def __init__(self):
        pass

    @staticmethod
    def get_comment_list():
        comment_list = CommentCollection.get_comment_list()
        i = 0
        comment_list_copy = []
        for comment in comment_list:
            comment_copy = {}
            comment_copy.update({
                "_id": str(comment.get('_id')),
                "title": comment.get("title"),
            })
            comment_list_copy.append(comment_copy)
            i += 1
        # print category_list_copy
        return comment_list_copy

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
    def add_comment(comment):
        CommentCollection.add_comment(comment)
        #
        # @staticmethod
        # def update_article(article):
        #     ArticleDB.update_article(article)
