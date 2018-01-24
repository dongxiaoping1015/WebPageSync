"""
Config module.
"""
from .develop import DevelopmentConfig

CONFIG = {
    'develop': DevelopmentConfig,
    'production': DevelopmentConfig,
    'test': DevelopmentConfig
}
