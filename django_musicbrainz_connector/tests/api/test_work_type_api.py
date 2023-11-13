from django_musicbrainz_connector.api.work_type import WorkTypeSerializer
from django_musicbrainz_connector.models.work_type import WorkType


def test_work_type_serializer():
    instance = WorkType(name="foo")
    serializer = WorkTypeSerializer(instance=instance)

    assert serializer.data["name"] == "foo"
