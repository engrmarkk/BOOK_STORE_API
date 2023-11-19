import os


class Config:
    # set the database URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # set the secret key
    SECRET_KEY = 'secret'
    # set JWT expiry time
    JWT_ACCESS_TOKEN_EXPIRES = False
    # set JWT blacklist
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///book_api.db'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///book_api.db'
    DEBUG = True


config_dict = {
    'test': TestConfig,
    'production': ProductionConfig,
    'development': DevelopmentConfig
}
