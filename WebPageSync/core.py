"""
app 入口模块
"""

import importlib
import logging
import os

from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from config import CONFIG

db = SQLAlchemy()


def create_app(config_name, register_blueprint=True):
    """
    创建应用实例
    """
    app = Flask(__name__)
    app.config.from_object(CONFIG[config_name])

    if not register_blueprint:
        return app

    config_logging(app)

    db.init_app(app)

    blue_config = (
        ('web.base_api', '/api'),
    )

    register_views(app, blue_config)

    return app


def register_views(app, configs):
    """
    注册视图函数
    """
    for blue, path in configs:
        if isinstance(blue, str):
            blues = blue.split('.')
            module = importlib.import_module('.'.join(blues[:-1]))
            name = blues[-1]
            if hasattr(module, name):
                blue = getattr(module, name)
            else:
                blue = None

        if blue:
            app.register_blueprint(blue, url_prefix=path)


def config_logging(app):
    """
    配置日志记录功能.
    """
    path = os.path.join(os.path.curdir, __package__, 'log')
    if not os.path.exists(path):
        os.makedirs(path)

    handler = RotatingFileHandler(
        os.path.join(path, 'web.log'), maxBytes=100000000, backupCount=10
    )
    if app.debug:
        handler.setLevel(logging.DEBUG)
    else:
        handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '[%(asctime)s]:%(levelname)s:%(pathname)s:%(lineno)d:%(message)s'
    )
    handler.setFormatter(formatter)
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(handler)


class ModelBase(object):
    """
    Base Model class.
    """
    __table_args__ = {"useexisting": True}

    def add_session(self):
        """
        Add model to session.
        """
        db.session.add(self)

    def save(self):
        """
        Save model to database.
        """
        self.add_session()
        self.commit()

    def commit(self):
        """
        Commit model to database.
        """
        from flask import current_app
        logger = current_app.logger
        try:
            db.session.commit()
        except SQLAlchemyError as err:
            db.session.rollback()
            logger.error(err)
            raise err
        except Exception as error:
            db.session.rollback()
            raise error

        return self

    def delete(self):
        """
        删除某条记录
        """
        db.session.delete(self)
