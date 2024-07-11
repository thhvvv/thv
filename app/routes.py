from flask import render_template
from app import app
from .news_api import get_sources, get_articles

@app.route('/')
def index():
    sources = get_sources('general')
    return render_template('index.html', sources=sources)

@app.route('/source/<id>')
def source(id):
    articles = get_articles(id)
    return render_template('article.html', articles=articles)
