import pytest
from app.models import Articles, Source

def test_articles_model():
    # Create an instance of the Articles model
    article = Articles(author='John Doe', title='Sample Article', description='Testing article', 
                       url='http://example.com', urlToImage='http://example.com/image.jpg', 
                       publishedAt='2024-07-05T12:00:00Z', content='Sample content')

    # Test individual attributes
    assert article.author == 'John Doe'
    assert article.title == 'Sample Article'
    assert article.description == 'Testing article'
    assert article.url == 'http://example.com'
    assert article.urlToImage == 'http://example.com/image.jpg'
    assert article.publishedAt == '2024-07-05T12:00:00Z'
    assert article.content == 'Sample content'

def test_source_model():
    # Create an instance of the Source model
    source = Source(id='abc-news', name='ABC News', description='Sample news source', 
                    url='http://abcnews.com', category='General')

    # Test individual attributes
    assert source.id == 'abc-news'
    assert source.name == 'ABC News'
    assert source.description == 'Sample news source'
    assert source.url == 'http://abcnews.com'
    assert source.category == 'General'
