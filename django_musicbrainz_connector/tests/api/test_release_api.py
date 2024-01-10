import pytest
from rest_framework.test import APIClient

RELEASE_RESPONSE = {
    "id": 2681644,
    "gid": "a026f47e-5ce7-4b6f-8469-cdf8c4bccb4b",
    "name": "Φάνταζες σαν πριγκηπέσα / Είσαι αριστοκράτισσα κι ωραία",
    "artist_credit": 205524,
    "release_group": 2369755,
    "status": 1,
    "packaging": None,
    "language": 159,
    "script": 22,
    "barcode": None,
    "comment": "",
    "edits_pending": 0,
    "quality": -1,
    "last_updated": "2023-11-10T14:02:54.412000-06:00",
}


@pytest.mark.django_db
def test_release_api_GET():
    api_client = APIClient()
    response = api_client.get("/api/releases/")
    assert response.status_code == 200
    assert response.data["count"] == 1
    assert response.data["next"] is None
    assert response.data["previous"] is None
    assert response.data["results"] == [RELEASE_RESPONSE]


@pytest.mark.django_db
def test_release_api_GET_by_id():
    api_client = APIClient()
    response = api_client.get("/api/releases/2681644/")
    assert response.status_code == 200
    assert response.data == RELEASE_RESPONSE


@pytest.mark.django_db
def test_release_api_GET_by_gid():
    api_client = APIClient()
    response = api_client.get("/api/releases/a026f47e-5ce7-4b6f-8469-cdf8c4bccb4b/")
    assert response.status_code == 200
    assert response.data == RELEASE_RESPONSE


@pytest.mark.django_db
def test_release_api_GET_not_found():
    api_client = APIClient()
    response = api_client.get("/api/releases/1/")
    assert response.status_code == 404
    assert response.data == {"detail": "Not found."}
