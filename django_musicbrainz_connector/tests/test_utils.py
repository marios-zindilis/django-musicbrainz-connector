import pytest

from django_musicbrainz_connector.utils import get_musicbrainz_identifier_type


@pytest.mark.parametrize(
    "identifier, expected_type",
    [
        (123, "id"),
    ],
)
def test_get_musicbrainz_identifier_type(identifier, expected_type):
    assert get_musicbrainz_identifier_type(identifier) == expected_type
