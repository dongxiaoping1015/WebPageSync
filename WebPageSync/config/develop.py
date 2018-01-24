"""
开发环境配置模块.
"""


class DevelopmentConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = ""  # 先写死，后面改写成读取文件
    SQLALCHEMY_BINDS = {}

    DATE_FORMAT = "%Y-%m-%d"
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    ONLINE_INTERVAL = 1800  # 用户操作一段时间没有有效操作就算不在线
    # 数据库连接池大小
    SQLALCHEMY_POOL_SIZE = 30

    DEBUG = True

    SQLALCHEMY_ECHO = False
