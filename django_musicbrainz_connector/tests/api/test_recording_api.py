import pytest
from rest_framework.test import APIClient

from django_musicbrainz_connector.api.recording import RecordingSerializer
from django_musicbrainz_connector.models import Recording

RECORDING_API_RESPONSE = {
    "id": 13679939,
    "gid": "fdb9d6f4-73f2-41f2-ba57-a8dbb65433a2",
    "name": "Αχάριστη",
    "length": 195000,
    "comment": "",
    "edits_pending": 0,
    "last_updated": "2023-11-10T14:02:54.412000-06:00",
    "video": False,
    "artist_credit": 1002760,
}


@pytest.mark.django_db
def test_recording_serializer():
    instance = Recording.objects.get(id=13679939)
    serializer = RecordingSerializer(instance=instance)

    assert serializer.data["name"] == "Αχάριστη"


@pytest.mark.django_db
def test_recording_api_GET():
    api_client = APIClient()
    response = api_client.get("/api/recordings/")
    assert response.status_code == 200
    assert response.data["count"] == 1
    assert response.data["next"] is None
    assert response.data["previous"] is None
    assert response.data["results"] == [RECORDING_API_RESPONSE]


@pytest.mark.django_db
def test_recording_api_GET_by_id():
    api_client = APIClient()
    response = api_client.get("/api/recordings/13679939/")
    assert response.status_code == 200
    assert response.data == RECORDING_API_RESPONSE


@pytest.mark.django_db
def test_recording_api_GET_by_gid():
    api_client = APIClient()
    response = api_client.get("/api/recordings/fdb9d6f4-73f2-41f2-ba57-a8dbb65433a2/")
    assert response.status_code == 200
    assert response.data == RECORDING_API_RESPONSE


@pytest.mark.django_db
def test_recording_api_GET_not_found():
    api_client = APIClient()
    response = api_client.get("/api/recordings/1/")
    assert response.status_code == 404
    assert response.data == {"detail": "Not found."}
