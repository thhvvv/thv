import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_route(client):
    # Test the index route '/'
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the News App" in response.data

# Add more tests for other routes as needed
