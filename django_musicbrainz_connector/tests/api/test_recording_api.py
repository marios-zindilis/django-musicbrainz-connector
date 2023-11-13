import pytest

from django_musicbrainz_connector.api.recording import RecordingSerializer
from django_musicbrainz_connector.models import Recording


@pytest.mark.django_db
def test_recording_serializer():
    instance = Recording.objects.get(id=13679939)
    serializer = RecordingSerializer(instance=instance)

    assert serializer.data["name"] == "Αχάριστη"
