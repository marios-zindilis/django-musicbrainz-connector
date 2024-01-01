import pytest

from django_musicbrainz_connector.models import Language


@pytest.mark.django_db
def test_language_str():
    language = Language.objects.get(id=159)
    assert str(language) == "Greek"
