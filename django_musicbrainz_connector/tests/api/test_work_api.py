import pytest

from django_musicbrainz_connector.api.work import WorkSerializer
from django_musicbrainz_connector.models.work import Work


@pytest.mark.django_db
def test_work_serializer():
    work = Work.objects.get(id=11432290)
    serializer = WorkSerializer(instance=work)

    assert serializer.data["name"] == "Η αχάριστη"
