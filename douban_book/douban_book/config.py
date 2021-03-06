"""
@Created by Seven on 2018-04-17
import os
from flask import (Flask,request....)
"""


class BaseConfig:
    USER_PER_PAGE = 10


class DevelopmentsConfig(BaseConfig):
    """
    开发环境
    """
    DEBUG = True
    SECRET_KEY = '7d58afd5-5fdb-48b0-9c99-3466c2838745'
    JSON_AS_ASCII = False


class TestingConfig:
    pass


class ProConfig:
    pass


configs = {
    'developments': DevelopmentsConfig,
    'testing': TestingConfig
}
