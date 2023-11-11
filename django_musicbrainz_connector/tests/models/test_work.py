from django_musicbrainz_connector.models import Work


def test_work_str():
    work = Work(name="foo")
    assert str(work) == "foo"
