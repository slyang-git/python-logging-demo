# -*- coding: utf-8 -*-

"""
Created by Bruce Yang on 17/11/8
"""
import logging
from logging import handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(name)s %(message)s')
file_handler = handlers.RotatingFileHandler('python-logging-demo.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.info('well done')
