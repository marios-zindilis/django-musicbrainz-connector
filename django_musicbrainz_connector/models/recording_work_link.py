"""
CREATE TABLE l_recording_work ( -- replicate
    id                  SERIAL,
    link                INTEGER NOT NULL, -- references link.id
    entity0             INTEGER NOT NULL, -- references recording.id
    entity1             INTEGER NOT NULL, -- references work.id
    edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
    last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    link_order          INTEGER NOT NULL DEFAULT 0 CHECK (link_order >= 0),
    entity0_credit      TEXT NOT NULL DEFAULT '',
    entity1_credit      TEXT NOT NULL DEFAULT ''
);
"""

from django.db import models


class RecordingWorkLink(models.Model):
    id = models.IntegerField("ID", primary_key=True, db_column="id")
    link = models.ForeignKey("Link", related_name="recording_work_links", on_delete=models.PROTECT, db_column="link")
    recording = models.ForeignKey(
        "Recording",
        verbose_name="Recording",
        related_name="work_links",
        on_delete=models.PROTECT,
        db_column="entity0",
    )
    work = models.ForeignKey(
        "Work",
        verbose_name="Work",
        related_name="recording_links",
        on_delete=models.PROTECT,
        db_column="entity1",
    )
    edits_pending = models.PositiveIntegerField("Edits Pending", db_column="edits_pending", default=0)
    last_updated = models.DateTimeField("Last Updated", db_column="last_updated")
    link_order = models.PositiveIntegerField(default=0, db_column="link_order")
    recording_credit = models.TextField("Recording Credit", db_column="entity0_credit")
    work_credit = models.TextField("Work Credit", db_column="entity1_credit")

    @property
    def link_type(self):
        return self.link.link_type

    class Meta:
        managed = False
        db_table = "l_recording_work"
        verbose_name_plural = "Recording Work Links"
