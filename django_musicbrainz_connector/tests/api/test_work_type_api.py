from django_musicbrainz_connector.api.work_type import WorkTypeSerializer
from django_musicbrainz_connector.models.work_type import WorkType


def test_work_type_serializer():
    work_type = WorkType(name="foo")
    serializer = WorkTypeSerializer(instance=work_type)

    assert serializer.data["name"] == "foo"
