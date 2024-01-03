import pytest
from rest_framework.test import APIClient

from django_musicbrainz_connector.api.artist_credit import ArtistCreditSerializer
from django_musicbrainz_connector.models.artist_credit import ArtistCredit


@pytest.mark.django_db
def test_artist_credit_serializer():
    instance = ArtistCredit.objects.get(id=1002760)
    serializer = ArtistCreditSerializer(instance=instance)

    assert serializer.data["name"] == "Ιωάννα Γεωργακοπούλου, Στελλάκης Περπινιάδης & Βασίλης Τσιτσάνης"


@pytest.mark.django_db
def test_artist_credit_GET():
    api_client = APIClient()
    response = api_client.get("/api/artist-credits/")
    assert response.status_code == 200
    assert response.data["count"] == 2
    assert response.data["next"] is None
    assert response.data["previous"] is None
    assert response.data["results"] == [
        {
            "id": 205524,
            "name": "Βασίλης Τσιτσάνης",
            "artist_count": 1,
            "ref_count": 336,
            "created": "2023-11-10T14:02:54.412000-06:00",
            "edits_pending": 0,
            "gid": "0e83e00a-a28c-3e80-9c00-5fa3d92cb2b1",
        },
        {
            "id": 1002760,
            "name": "Ιωάννα Γεωργακοπούλου, Στελλάκης Περπινιάδης & Βασίλης Τσιτσάνης",
            "artist_count": 3,
            "ref_count": 2,
            "created": "2023-11-10T14:02:54.412000-06:00",
            "edits_pending": 0,
            "gid": "8c9bafac-0df4-33c0-a7e2-61b4d5774936",
        },
    ]
