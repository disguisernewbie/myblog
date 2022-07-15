from flask import  Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_cors import CORS
from .utils.tools import ReConverter     # 导入正则转换器
import redis

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)
    app.config['JSON_AS_ASCII'] = False

    CORS(app, supports_credentials=True)

     # 利用 flask_session 将session保存再redis中
    Session(app)
    # 注册数据库引擎
    db.init_app(app)

    # 初始化redis的连接对象
    # global redis_store
    # redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

    # redis_store.set('count', 0)
    # redis_store.set('num', 1)
    # redis_store.expire('num', 86400)
    # redis_store.expire('count', 86400)

    # 为flask添加自定义的转换器
    app.url_map.converters['re'] = ReConverter
    
    from .V1 import b_user
    app.register_blueprint(b_user, url_prefix='/user')
    from .V1 import b_image
    app.register_blueprint(b_image, url_prefix='/image')

    return app