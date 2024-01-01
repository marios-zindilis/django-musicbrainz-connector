import pytest

from django_musicbrainz_connector.models import ReleasePackaging


@pytest.mark.django_db
def test_release_packaging_str():
    release_packaging = ReleasePackaging.objects.get(id=1)
    assert str(release_packaging) == "Jewel Case"
