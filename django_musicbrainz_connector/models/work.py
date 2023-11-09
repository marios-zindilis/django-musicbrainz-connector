from django.db import models


class Work(models.Model):
    """
        CREATE TABLE work ( -- replicate (verbose)
        id                  SERIAL,
        gid                 UUID NOT NULL,
        name                VARCHAR NOT NULL,
        type                INTEGER, -- references work_type.id
        comment             VARCHAR(255) NOT NULL DEFAULT '',
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );
    """

    id = models.IntegerField("ID", primary_key=True, db_column="id")
    gid = models.UUIDField(db_column="gid")
    name = models.CharField(max_length=255, db_column="name")
    type = models.ForeignKey("WorkType", db_column="type", on_delete=models.PROTECT)
    edits_pending = models.PositiveIntegerField("Edits Pending", db_column="edits_pending", default=0)
    last_updated = models.DateTimeField("Last Updated", db_column="last_updated")

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = "work"
        verbose_name_plural = "Works"
