import pytest

from django_musicbrainz_connector.models import Script


@pytest.mark.django_db
def test_script_str():
    script = Script.objects.get(id=22)
    assert str(script) == "Greek"
