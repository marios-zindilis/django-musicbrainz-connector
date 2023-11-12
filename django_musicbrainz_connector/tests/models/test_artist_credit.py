import pytest

from django_musicbrainz_connector.models.artist_credit import ArtistCredit


@pytest.mark.django_db
def test_artist_credit_str():
    artist_credit = ArtistCredit.objects.get(id=1002760)
    assert str(artist_credit) == "Ιωάννα Γεωργακοπούλου, Στελλάκης Περπινιάδης & Βασίλης Τσιτσάνης"
