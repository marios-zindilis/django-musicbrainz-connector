import pytest

from django_musicbrainz_connector.models import WorkType


@pytest.mark.django_db
def test_work_type_str():
    work_type = WorkType.objects.get(id=17)
    assert str(work_type) == "Song"
