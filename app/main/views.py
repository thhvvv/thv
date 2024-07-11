from flask import render_template, request
from . import main
from ..news_api import get_sources, get_articles

@main.route('/')
def index():
    sources = get_sources('general')
    return render_template('index.html', sources=sources)

@main.route('/source/<id>')
def source(id):
    articles = get_articles(id)
    return render_template('article.html', articles=articles)
