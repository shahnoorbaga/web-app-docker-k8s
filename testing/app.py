import pytest
import requests

def test_homepage():
    response = requests.get('http://web-app-frontend.frontend.svc.cluster.local:5000/')
    assert response.status_code == 200