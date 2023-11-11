from django_musicbrainz_connector.models import WorkType


def test_work_type_str():
    work_type = WorkType(name="foo")
    assert str(work_type) == "foo"
