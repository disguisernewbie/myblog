# coding:utf8
from werkzeug.routing import BaseConverter
from sqlalchemy.orm import class_mapper
from flask import session, jsonify, g
import functools
import re

# 时间模块
from datetime import datetime

# 初始化时间字符串
datetime_dt = datetime.today()  # 获取当前日期和时间
datetime_str = datetime_dt.strftime("%Y-%m-%d %H:%M:%S")  # 格式化日期时间

import redis

redis_host = 'localhost'
redis_port = 6379
redis_store = redis.StrictRedis(host=redis_host, port=redis_port, db=1)

class Tools:
    
    # orm 数据序列化
    def serialize(model):
        if type(model) == list:
            datalist = []
            for m in model:
                columns = [c.key for c in class_mapper(m.__class__).columns]
                data = dict((c, getattr(m, c)) for c in columns)
                datalist.append(data)
            return datalist
        else:
            columns = [c.key for c in class_mapper(model.__class__).columns]
            return dict((c, getattr(model, c)) for c in columns) 

# 定义正则转换器
class ReConverter(BaseConverter):
    """获取get中url任意正则的转换器"""
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(BaseConverter, self).__init__()
        # 保存正则表达式
        self.regex = regex

# jwt验证
def jwt_auth(view_func):
    @functools.wraps(view_func)
    def wrapper(*args, **kwargs):
        
        return view_func(*args ,**kwargs)
    return wrapper

# 登录验证
def login_required(role):
    def login(view_Func):
        def wrapper(*args, **kwargs):

            return view_Func(*args, **kwargs)
        return wrapper

    return login
