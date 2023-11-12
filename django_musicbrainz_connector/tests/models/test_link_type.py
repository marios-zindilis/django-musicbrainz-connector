import pytest

from django_musicbrainz_connector.models.link_type import LinkType


@pytest.mark.django_db
def test_link_type_str():
    link_type = LinkType.objects.get(id=278)
    assert str(link_type) == "performance: recording -> work"
