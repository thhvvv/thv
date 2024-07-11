from flask import render_template, request
from . import main_bp
from ..news_api import get_sources, get_articles

@main_bp.route('/')
def index():
    sources = get_sources('general')
    return render_template('index.html', sources=sources)

@main_bp.route('/source/<id>')
def source(id):
    articles = get_articles(id)
    return render_template('article.html', articles=articles)
