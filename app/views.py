from flask import render_template, jsonify, request
from . import app, db  # Assuming 'app' is the Flask application instance and 'db' is the SQLAlchemy instance
from .models import Article, Source

# Example route for rendering a template
@app.route('/')
def index():
    sources = Source.query.all()  # Fetch all news sources from the database
    return render_template('index.html', sources=sources)

# Example route for fetching articles from a source
@app.route('/source/<int:source_id>')
def source_articles(source_id):
    source = Source.query.get_or_404(source_id)  # Retrieve the source by ID or return 404 if not found
    articles = Article.query.filter_by(source_id=source.id).all()  # Fetch articles for the specified source
    return render_template('articles.html', source=source, articles=articles)

# Example API route for fetching articles in JSON format
@app.route('/api/source/<int:source_id>/articles', methods=['GET'])
def api_source_articles(source_id):
    source = Source.query.get_or_404(source_id)  # Retrieve the source by ID or return 404 if not found
    articles = Article.query.filter_by(source_id=source.id).all()  # Fetch articles for the specified source
    article_list = [{'title': article.title, 'author': article.author, 'content': article.content} for article in articles]
    return jsonify({'source': source.name, 'articles': article_list})

# Example route for saving an article (requires form submission and processing)
@app.route('/save_article', methods=['POST'])
def save_article():
    article_id = request.form.get('article_id')
    # Logic to save the article ID to a user's saved articles list
    return jsonify({'message': 'Article saved successfully'})

# Example route for handling errors (404 Not Found)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Additional routes and logic as per application requirements
