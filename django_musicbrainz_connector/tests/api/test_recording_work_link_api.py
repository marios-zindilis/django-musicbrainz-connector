import pytest

from django_musicbrainz_connector.api.recording_work_link import RecordingWorkLinkSerializer
from django_musicbrainz_connector.models.work import RecordingWorkLink


@pytest.mark.django_db
def test_recording_work_link_serializer():
    instance = RecordingWorkLink.objects.get(id=606936)
    serializer = RecordingWorkLinkSerializer(instance=instance)

    assert serializer.data["recording"] == 13679939
