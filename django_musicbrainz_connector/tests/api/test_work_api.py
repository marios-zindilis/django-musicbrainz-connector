from django_musicbrainz_connector.api.work import WorkSerializer
from django_musicbrainz_connector.models.work import Work


def test_work_serializer():
    work = Work(name="foo")
    serializer = WorkSerializer(instance=work)

    assert serializer.data["name"] == "foo"
