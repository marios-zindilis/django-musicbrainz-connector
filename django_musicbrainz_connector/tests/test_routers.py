from unittest import mock

from django_musicbrainz_connector.routers import DjangoMusicBrainzConnectorDatabaseRouter

FAKE_MODEL_IN_DJANGO_MUSICBRAINZ_CONNECTOR_1 = mock.Mock(
    _meta=mock.Mock(
        app_label="django_musicbrainz_connector",
    )
)

FAKE_MODEL_IN_DJANGO_MUSICBRAINZ_CONNECTOR_2 = mock.Mock(
    _meta=mock.Mock(
        app_label="django_musicbrainz_connector",
    )
)

FAKE_MODEL_IN_DIFFERENT_APP = mock.Mock(
    _meta=mock.Mock(
        app_label="foo",
    )
)


def test_django_musicbrainz_connector_database_router():
    router = DjangoMusicBrainzConnectorDatabaseRouter()

    assert router.db_for_read(FAKE_MODEL_IN_DJANGO_MUSICBRAINZ_CONNECTOR_1) == "musicbrainz_db"
    assert router.db_for_write(FAKE_MODEL_IN_DJANGO_MUSICBRAINZ_CONNECTOR_1) == "musicbrainz_db"

    assert router.db_for_read(FAKE_MODEL_IN_DIFFERENT_APP) is None
    assert router.db_for_write(FAKE_MODEL_IN_DIFFERENT_APP) is None

    assert (
        router.allow_relation(
            FAKE_MODEL_IN_DJANGO_MUSICBRAINZ_CONNECTOR_1,
            FAKE_MODEL_IN_DJANGO_MUSICBRAINZ_CONNECTOR_2,
        )
        is True
    )
    assert (
        router.allow_relation(
            FAKE_MODEL_IN_DJANGO_MUSICBRAINZ_CONNECTOR_1,
            FAKE_MODEL_IN_DIFFERENT_APP,
        )
        is None
    )

    assert router.allow_migrate("fake_db", "django_musicbrainz_connector") is False
    assert router.allow_migrate("fake_db", "foo") is None
