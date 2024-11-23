import pytest
import requests

#Testing the frontend
def test_homepage():
    response = requests.get('http://web-app-frontend.frontend.svc.cluster.local/')
    assert response.status_code == 200

#Testing backend insert functionality
def test_submit_data():
    # Test successful submission
    response = requests.post('http://web-app-backend.backend.svc.cluster.local:5000/submit', json={'name': 'John Doe', 'email': 'john@example.com'})
    assert response.status_code == 200
    #assert response.json == {"message": "Data submitted successfully"}

    # Test missing name
    response = requests.post('http://web-app-backend.backend.svc.cluster.local:5000/submit', json={'email': 'john@example.com'})
    assert response.status_code == 400
    #assert response.json == {"message": "Name and email are required"}

    # Test missing email
    response = requests.post('http://web-app-backend.backend.svc.cluster.local:5000/submit', json={'name': 'John Doe'})
    assert response.status_code == 400
    #assert response.json == {"message": "Name and email are required"}
