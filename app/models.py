# -*- coding: utf-8 -*-


"""
Created by yangshuanglong@wecash.net on 2017/11/9
"""
import logging


logger = logging.getLogger(__name__)


class User(object):
    def __init__(self, name):
        logger.info('log in __init__')
        self.name = name

    def get_name(self):
        logger.info('log in get_name')
        return self.name

