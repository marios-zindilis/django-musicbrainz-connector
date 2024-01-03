import pytest

from django_musicbrainz_connector.models import Release


@pytest.mark.django_db
def test_release_str():
    release = Release.objects.get(id=2681644)
    assert str(release) == "Φάνταζες σαν πριγκηπέσα / Είσαι αριστοκράτισσα κι ωραία"
