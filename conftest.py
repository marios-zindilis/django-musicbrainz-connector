import pytest
from django.apps import apps
from django.core.management import call_command

from django_musicbrainz_connector.apps import DjangoMusicbrainzConnectorConfig


@pytest.mark.django_db
def pytest_sessionstart():
    """Convert unmanaged models to managed models during testing, so we can create objects in a test database."""
    unmanaged_models = [
        model
        for model in apps.get_app_config(DjangoMusicbrainzConnectorConfig.name).get_models()
        if model._meta.managed is False
    ]
    for model in unmanaged_models:
        model._meta.managed = True


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "django_musicbrainz_connector/tests/fixtures/link-type.json")
        call_command("loaddata", "django_musicbrainz_connector/tests/fixtures/link.json")
        call_command("loaddata", "django_musicbrainz_connector/tests/fixtures/work-type.json")
        call_command("loaddata", "django_musicbrainz_connector/tests/fixtures/work.json")
        call_command("loaddata", "django_musicbrainz_connector/tests/fixtures/artist-credit.json")
        call_command("loaddata", "django_musicbrainz_connector/tests/fixtures/recording.json")
        call_command("loaddata", "django_musicbrainz_connector/tests/fixtures/recording-work-link.json")
        call_command("loaddata", "django_musicbrainz_connector/tests/fixtures/script.json")
        call_command("loaddata", "django_musicbrainz_connector/tests/fixtures/language.json")
        call_command("loaddata", "django_musicbrainz_connector/tests/fixtures/release-packaging.json")
        call_command("loaddata", "django_musicbrainz_connector/tests/fixtures/release-status.json")
