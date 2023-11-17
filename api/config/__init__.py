import os


class Config:
    # set the database URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # set the secret key
    SECRET_KEY = 'secret'


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
