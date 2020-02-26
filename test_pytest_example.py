import requests
import pytest

pytest.url = "http://localhost:8080/api/values"

def test_success():
    response = requests.get(pytest.url)
    print(response.text)
    assert response.status_code == 200
    assert response.text == '[{"id":1,"colourName":"Red"},{"id":2,"colourName":"Orange"},{"id":3,"colourName":"Yellow"},{"id":4,"colourName":"Green"},{"id":5,"colourName":"Blue"}]'
    
