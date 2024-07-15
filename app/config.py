import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    NEWS_API_KEY = os.environ.get('NYT_API_KEY')
    NYT_TOP_STORIES_URL = 'https://api.nytimes.com/svc/topstories/v2/{}.json?api-key={}'
    NYT_ARTICLE_URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={}&api-key={}'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

config_options = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
