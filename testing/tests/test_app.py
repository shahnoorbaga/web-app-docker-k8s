import pytest
import requests

def test_homepage():
    response = requests.get('http://web-app-frontend.frontend.svc.cluster.local/')
    assert response.status_code == 200

def test_example():
    assert 1 + 1 == 2
