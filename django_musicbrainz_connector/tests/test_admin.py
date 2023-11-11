from unittest import mock

from django_musicbrainz_connector.admin import WorkAdmin, WorkType, admin


def test_django_musicbrainz_connector_model_admin():
    work_admin = WorkAdmin(WorkType, admin.site)
    assert work_admin.has_change_permission(request=mock.Mock()) is False
    assert work_admin.has_delete_permission(request=mock.Mock()) is False
    assert work_admin.has_add_permission(request=mock.Mock()) is False
