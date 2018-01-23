"""
Config module.
"""
from .develop import DevelopmentConfig

CONFIG = {
    'development': DevelopmentConfig,
    'production': DevelopmentConfig,
    'test': DevelopmentConfig
}
