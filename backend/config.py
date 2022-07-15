# coding:utf-8
import redis

#获取绝对路径

class Config():
    """配置文件基类"""
    SECRET_KEY = 'RMVVS'  # 项目密钥
    # 服务器数据库
    # SQLALCHEMY_DATABASE_URI = "mysql://root:123456@192.168.1.102:3306/v"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
    # # 打开数据库语句自动提交
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_POOL_SIZE = 50

    # # redis配置
    # REDIS_HOST = '127.0.0.1'
    # REDIS_PORT = 6379

    # session配置，使用redis
    # SESSION_TYPE = 'redis'
    # SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # 度cookie进行隐藏
    PERMANENT_SESSION_LIFETIME = 86400  # 设置有效期 单位秒


class DevelopmentConfig(Config):
    """开发环境"""
    DEBUG = True


class ProductConfig(Config):
    """生产环境"""
    pass


# 使用该字典获取相应的配置文件
config_map = {
    'develop': DevelopmentConfig,
    'product': ProductConfig
}