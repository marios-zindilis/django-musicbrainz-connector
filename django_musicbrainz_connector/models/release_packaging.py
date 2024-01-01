"""
CREATE TABLE release_packaging ( -- replicate
    id                  SERIAL,
    name                VARCHAR(255) NOT NULL,
    parent              INTEGER, -- references release_packaging.id
    child_order         INTEGER NOT NULL DEFAULT 0,
    description         TEXT,
    gid                 uuid NOT NULL
);
"""

from django.db import models


class ReleasePackaging(models.Model):
    id = models.IntegerField("ID", primary_key=True, db_column="id")
    name = models.CharField("Name", max_length=255, db_column="name")
    parent = models.ForeignKey("self", db_column="parent", null=True, on_delete=models.PROTECT)
    child_order = models.IntegerField("Child Order", db_column="child_order")
    description = models.TextField("Description", db_column="description")
    gid = models.UUIDField(db_column="gid")

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "release_packaging"
        verbose_name_plural = "Release Packaging"
        ordering = ["name"]
