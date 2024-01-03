"""
CREATE TABLE release ( -- replicate (verbose)
    id                  SERIAL,
    gid                 UUID NOT NULL,
    name                VARCHAR NOT NULL,
    artist_credit       INTEGER NOT NULL, -- references artist_credit.id
    release_group       INTEGER NOT NULL, -- references release_group.id
    status              INTEGER, -- references release_status.id
    packaging           INTEGER, -- references release_packaging.id
    language            INTEGER, -- references language.id
    script              INTEGER, -- references script.id
    barcode             VARCHAR(255),
    comment             VARCHAR(255) NOT NULL DEFAULT '',
    edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
    quality             SMALLINT NOT NULL DEFAULT -1,
    last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
"""

from django.db import models


class Release(models.Model):
    id = models.IntegerField("ID", primary_key=True, db_column="id")
    gid = models.UUIDField("GID", db_column="gid")
    name = models.CharField(max_length=2048, db_column="name")
    artist_credit = models.ForeignKey(
        "ArtistCredit",
        verbose_name="Artist Credit",
        related_name="releases",
        on_delete=models.PROTECT,
        db_column="artist_credit",
    )
    release_group = models.ForeignKey(
        "ReleaseGroup",
        verbose_name="Release Group",
        related_name="releases",
        on_delete=models.PROTECT,
        db_column="release_group",
    )
    status = models.ForeignKey(
        "ReleaseStatus",
        verbose_name="Status",
        related_name="releases",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        db_column="status",
    )
    packaging = models.ForeignKey(
        "ReleasePackaging",
        verbose_name="Packaging",
        related_name="releases",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        db_column="packaging",
    )
    language = models.ForeignKey(
        "Language",
        verbose_name="Language",
        related_name="Releases",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        db_column="language",
    )
    script = models.ForeignKey(
        "Script",
        verbose_name="Script",
        related_name="releases",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        db_column="script",
    )
    barcode = models.CharField("BarCode", max_length=255, null=True, blank=True, db_column="barcode")
    comment = models.CharField("Comment", max_length=255, default="", db_column="comment")
    edits_pending = models.PositiveIntegerField("Edits Pending", db_column="edits_pending", default=0)
    quality = models.SmallIntegerField("Quality", default=-1, db_column="quality")
    last_updated = models.DateTimeField("Last Updated", db_column="last_updated")

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = "release"
        verbose_name_plural = "Releases"
        ordering = ["name"]
