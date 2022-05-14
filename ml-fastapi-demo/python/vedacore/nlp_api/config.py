import os


class Config:
    ENV = os.environ.get('ENV', 'development')
    DEBUG = True


class ProdConfig(Config):
    ENV = 'production'
    DEBUG = False
    TESTING = False
    # other config for production
