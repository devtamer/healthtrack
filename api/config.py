import os

class BaseConfig:
    """Base Configuration"""
    SECRET_KEY = 'SuperSecretKey'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:yourpassword@localhost/health'
    DEBUG = True
    CORS_HEADERS = 'Content-Type'


class DevelopmentConfig(BaseConfig):
    """Development Configuration"""
    SECRET_KEY = 'SuperSecretKey'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:yourpassword@localhost/health'
    DEBUG = True

class TestingConfig(BaseConfig):
    """Testing Configuration"""
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False