import pytest
from rest_framework.test import APIClient

EXPECTED_MEDIUM_API_RESPONSE = {
    "id": 2912288,
    "position": 1,
    "name": "",
    "edits_pending": 0,
    "last_updated": "2020-04-19T12:53:28.789455-05:00",
    "track_count": 2,
    "release": 2681644,
    "format": 73,
}


@pytest.mark.django_db
def test_medium_api_GET():
    api_client = APIClient()
    response = api_client.get("/api/media/")
    assert response.status_code == 200
    assert response.data["count"] == 1
    assert response.data["next"] is None
    assert response.data["previous"] is None
    assert response.data["results"] == [EXPECTED_MEDIUM_API_RESPONSE]


@pytest.mark.django_db
def test_medium_api_GET_by_release():
    api_client = APIClient()
    response = api_client.get("/api/media/?release-id=2681644")
    assert response.status_code == 200
    assert response.data["count"] == 1
    assert response.data["next"] is None
    assert response.data["previous"] is None
    assert response.data["results"] == [EXPECTED_MEDIUM_API_RESPONSE]


@pytest.mark.django_db
def test_medium_api_GET_by_non_existent_release():
    api_client = APIClient()
    response = api_client.get("/api/media/?release-id=1234")
    assert response.status_code == 200
    assert response.data["count"] == 0
    assert response.data["next"] is None
    assert response.data["previous"] is None
    assert response.data["results"] == []
