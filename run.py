# -*- coding: utf-8 -*-


"""
Created by BruceYang on 2017/11/9
"""
import logging

from app.models import User
from app.services import logger
from app.views import logger
from app.utils.idcard_verify import logger

user = User('yang')

user.get_name()

print(logging.Logger.manager.loggerDict)

