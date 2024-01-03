import pytest

from django_musicbrainz_connector.models import ReleaseGroupPrimaryType


@pytest.mark.django_db
def test_release_packaging_str():
    release_packaging = ReleaseGroupPrimaryType.objects.get(id=1)
    assert str(release_packaging) == "Album"
