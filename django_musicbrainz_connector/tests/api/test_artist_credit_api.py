import pytest

from django_musicbrainz_connector.api.artist_credit import ArtistCreditSerializer
from django_musicbrainz_connector.models.artist_credit import ArtistCredit


@pytest.mark.django_db
def test_artist_credit_serializer():
    artist_credit = ArtistCredit.objects.get(id=1002760)
    serializer = ArtistCreditSerializer(instance=artist_credit)

    assert serializer.data["name"] == "Ιωάννα Γεωργακοπούλου, Στελλάκης Περπινιάδης & Βασίλης Τσιτσάνης"
