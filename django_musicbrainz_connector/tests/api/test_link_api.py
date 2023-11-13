import pytest

from django_musicbrainz_connector.api.link import LinkSerializer
from django_musicbrainz_connector.models.link import Link


@pytest.mark.django_db
def test_link_serializer():
    link = Link.objects.get(id=51696)
    serializer = LinkSerializer(instance=link)

    assert serializer.data["begin_date_year"] == 1947
