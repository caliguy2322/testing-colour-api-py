import requests
import pytest

pytest.url = "http://colour_api:80/api/values"


def test_success():
    response = requests.get(pytest.url)
    expected = '[{"id":1,"colourName":"Red"},{"id":2,"colourName":"Orange"},{"id":3,"colourName":"Yellow"},{"id":4,"colourName":"Green"},{"id":5,"colourName":"Blue"}]'
    assert response.status_code == 200
    assert response.text == expected
