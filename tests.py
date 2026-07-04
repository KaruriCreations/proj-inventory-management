import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_all_items(client):
    response = client.get('/inventory')
    assert response.status_code == 200
    assert isinstance(response.json['inventory'], list)

def test_get_item(client):
    # Add a dummy item to the inventory and grab its ID
    post_res = client.post('/inventory', json={'name': 'Test Item', 'price': 100})
    assert post_res.status_code == 201
    item_id = post_res.json['item']['id']
    
    # Fetch that exact item
    response = client.get(f'/inventory/{item_id}')
    assert response.status_code == 200
    assert response.json['item']['name'] == 'Test Item'
    assert response.json['item']['price'] == 100


def test_create_item(client):
    response = client.post('/inventory', json={'name': 'Test Item', 'price': 100})
    assert response.status_code == 201
    assert response.json['item']['name'] == 'Test Item'
    assert response.json['item']['price'] == 100

def test_update_item(client):
    # Add a dummy item to the inventory and grab its ID
    post_res = client.post('/inventory', json={'name': 'Test Item', 'price': 100})
    assert post_res.status_code == 201
    item_id = post_res.json['item']['id']

    # Update that exact item
    response = client.patch(f'/inventory/{item_id}', json={'name': 'Test Item Updated', 'price': 200})
    assert response.status_code == 200
    assert response.json['item']['name'] == 'Test Item Updated'
    assert response.json['item']['price'] == 200
    

def test_delete_item(client):
    # Add a dummy item to the inventory and grab its ID
    post_res = client.post('/inventory', json={'name': 'Test Item', 'price': 100})
    assert post_res.status_code == 201
    item_id = post_res.json['item']['id']

    # Delete that exact item
    response = client.delete(f'/inventory/{item_id}')
    assert response.status_code == 200
