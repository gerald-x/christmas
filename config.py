class Config(object):
    FLASK_ENV = 'development'
    ENV = 'development'
    DEBUG = True
    TESTING = True
    SESSION_COOKIE_SECURE = True

class productionConfig(Config):
    FLASK_ENV = 'production'
    ENV = 'production'
    DEBUG = False
    TESTING = True
    SESSION_COOKIE_SECURE = True