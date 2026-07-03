import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_all_items(client):
    pass

def test_get_item(client):
    pass

def test_create_item(client):
    pass

def test_update_item(client):
    pass

def test_delete_item(client):
    pass
