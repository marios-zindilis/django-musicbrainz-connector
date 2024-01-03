import pytest

from django_musicbrainz_connector.models import Track


@pytest.mark.django_db
def test_track_str():
    track = Track.objects.get(id=31083305)
    assert str(track) == "Φάνταζες σαν πριγκηπέσα"
