import pytest


def test_root(myapp):
    response = myapp.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}