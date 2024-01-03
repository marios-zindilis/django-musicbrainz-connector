import pytest

from django_musicbrainz_connector.models import MediumFormat


@pytest.mark.django_db
def test_medium_format_str():
    medium_format = MediumFormat.objects.get(id=73)
    assert str(medium_format) == "Phonograph record"
