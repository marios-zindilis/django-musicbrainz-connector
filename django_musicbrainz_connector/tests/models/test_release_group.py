import pytest

from django_musicbrainz_connector.models import ReleaseGroup


@pytest.mark.django_db
def test_release_group_str():
    release_group = ReleaseGroup.objects.get(id=2369755)
    assert str(release_group) == "Φάνταζες σαν πριγκηπέσα / Είσαι αριστοκράτισσα κι ωραία"
