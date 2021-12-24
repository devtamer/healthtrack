import os

class BaseConfig:
    """Base Configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'foobar')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') 
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    CORS_HEADERS = 'Content-Type'
    
class DevelopmentConfig(BaseConfig):
    """Development Configuration"""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4

class TestingConfig(BaseConfig):
    """Testing Configuration"""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    PRESERVE_CONTEXT_ON_EXCEPTION = False