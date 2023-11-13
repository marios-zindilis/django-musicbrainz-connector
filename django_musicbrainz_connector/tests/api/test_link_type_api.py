import pytest

from django_musicbrainz_connector.api.link_type import LinkTypeSerializer
from django_musicbrainz_connector.models.link_type import LinkType


@pytest.mark.django_db
def test_link_type_serializer():
    link_type = LinkType.objects.get(id=278)
    serializer = LinkTypeSerializer(instance=link_type)

    assert serializer.data["name"] == "performance"
