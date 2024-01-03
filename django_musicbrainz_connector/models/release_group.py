"""
CREATE TABLE release_group ( -- replicate (verbose)
    id                  SERIAL,
    gid                 UUID NOT NULL,
    name                VARCHAR NOT NULL,
    artist_credit       INTEGER NOT NULL, -- references artist_credit.id
    type                INTEGER, -- references release_group_primary_type.id
    comment             VARCHAR(255) NOT NULL DEFAULT '',
    edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
    last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
"""

from django.db import models


class ReleaseGroup(models.Model):
    id = models.IntegerField("ID", primary_key=True, db_column="id")
    gid = models.UUIDField("GID", db_column="gid")
    name = models.CharField(max_length=2048, db_column="name")
    artist_credit = models.ForeignKey(
        "ArtistCredit",
        verbose_name="Artist Credit",
        related_name="release_groups",
        on_delete=models.PROTECT,
        db_column="artist_credit",
    )
    type = models.ForeignKey(
        "ReleaseGroupPrimaryType",
        verbose_name="Type",
        related_name="release_groups",
        on_delete=models.PROTECT,
        db_column="type",
    )
    comment = models.CharField("Comment", max_length=255, default="", db_column="comment")
    edits_pending = models.PositiveIntegerField("Edits Pending", db_column="edits_pending", default=0)
    last_updated = models.DateTimeField("Last Updated", db_column="last_updated")

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = "release_group"
        verbose_name_plural = "Release Groups"
        ordering = ["name"]
