import pytest

from django_musicbrainz_connector.models import ReleaseStatus


@pytest.mark.django_db
def test_release_status_str():
    release_status = ReleaseStatus.objects.get(id=1)
    assert str(release_status) == "Official"
