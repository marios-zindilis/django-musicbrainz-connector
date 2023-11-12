import pytest

from django_musicbrainz_connector.models import LinkType, RecordingWorkLink


@pytest.mark.django_db
def test_recording_work_link_type():
    recording_work_link = RecordingWorkLink.objects.get(id=606936)
    link_type = LinkType.objects.get(id=278)
    assert recording_work_link.link_type == link_type
