import pytest

from django_musicbrainz_connector.models import Medium


@pytest.mark.django_db
def test_medium_str():
    medium = Medium.objects.get(id=2912288)
    assert str(medium) == ""
