# Generated by Django 4.2.7 on 2023-11-12 10:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_musicbrainz_connector", "0002_work"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArtistCredit",
            fields=[
                ("id", models.IntegerField(db_column="id", primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(db_column="name", max_length=255, verbose_name="Name")),
                ("artist_count", models.SmallIntegerField(db_column="artist_count", verbose_name="Artist Count")),
                ("ref_count", models.IntegerField(db_column="ref_count", verbose_name="Ref Count")),
                ("created", models.DateTimeField(db_column="created", verbose_name="Created")),
                (
                    "edits_pending",
                    models.PositiveIntegerField(db_column="edits_pending", default=0, verbose_name="Edits Pending"),
                ),
                ("gid", models.UUIDField(db_column="gid", verbose_name="GID")),
            ],
            options={
                "verbose_name_plural": "Artist Credits",
                "db_table": "artist_credit",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Link",
            fields=[
                ("id", models.IntegerField(db_column="id", primary_key=True, serialize=False, verbose_name="ID")),
                ("begin_date_year", models.SmallIntegerField(null=True, verbose_name="Begin Date Year")),
                ("begin_date_month", models.SmallIntegerField(null=True, verbose_name="Begin Date Month")),
                ("begin_date_day", models.SmallIntegerField(null=True, verbose_name="Begin Date Day")),
                ("end_date_year", models.SmallIntegerField(null=True, verbose_name="End Date Year")),
                ("end_date_month", models.SmallIntegerField(null=True, verbose_name="End Date Month")),
                ("end_date_day", models.SmallIntegerField(null=True, verbose_name="End Date Day")),
                ("attribute_count", models.IntegerField(default=0, verbose_name="Attribute Count")),
                ("created", models.DateTimeField(db_column="created", verbose_name="Created")),
                ("ended", models.BooleanField(default=False, verbose_name="Ended?")),
            ],
            options={
                "verbose_name_plural": "Links",
                "db_table": "link",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="LinkType",
            fields=[
                ("id", models.IntegerField(db_column="id", primary_key=True, serialize=False, verbose_name="ID")),
                ("child_order", models.IntegerField(db_column="child_order", verbose_name="Child Order")),
                ("gid", models.UUIDField(db_column="gid", verbose_name="GID")),
                ("entity_type0", models.CharField(max_length=50, verbose_name="Entity Type 0")),
                ("entity_type1", models.CharField(max_length=50, verbose_name="Entity Type 1")),
                ("name", models.CharField(db_column="name", max_length=255)),
                ("description", models.TextField(db_column="description")),
                ("link_phrase", models.CharField(db_column="link_phrase", max_length=255, verbose_name="Link Phrase")),
                (
                    "reverse_link_phrase",
                    models.CharField(
                        db_column="reverse_link_phrase", max_length=255, verbose_name="Reverse Link Phrase"
                    ),
                ),
                (
                    "long_link_phrase",
                    models.CharField(db_column="long_link_phrase", max_length=255, verbose_name="Long Link Phrase"),
                ),
                ("priority", models.IntegerField(default=0)),
                ("last_updated", models.DateTimeField(db_column="last_updated", verbose_name="Last Updated")),
                ("is_deprecated", models.BooleanField(default=False, verbose_name="Is Deprecated?")),
                ("has_dates", models.BooleanField(default=True, verbose_name="Has Dates?")),
                ("entity0_cardinality", models.SmallIntegerField(default=0, verbose_name="Entity 0 Cardinality")),
                ("entity1_cardinality", models.SmallIntegerField(default=0, verbose_name="Entity 1 Cardinality")),
            ],
            options={
                "verbose_name_plural": "Link Types",
                "db_table": "link_type",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Recording",
            fields=[
                ("id", models.IntegerField(db_column="id", primary_key=True, serialize=False, verbose_name="ID")),
                ("gid", models.UUIDField(db_column="gid", verbose_name="GID")),
                ("name", models.CharField(db_column="name", max_length=255)),
                ("length", models.PositiveIntegerField(db_column="length", null=True)),
                ("comment", models.CharField(db_column="comment", default="", max_length=255, verbose_name="Comment")),
                (
                    "edits_pending",
                    models.PositiveIntegerField(db_column="edits_pending", default=0, verbose_name="Edits Pending"),
                ),
                ("last_updated", models.DateTimeField(db_column="last_updated", verbose_name="Last Updated")),
                ("video", models.BooleanField(db_column="video", default=False)),
            ],
            options={
                "verbose_name_plural": "Recordings",
                "db_table": "recording",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="RecordingWorkLink",
            fields=[
                ("id", models.IntegerField(db_column="id", primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "edits_pending",
                    models.PositiveIntegerField(db_column="edits_pending", default=0, verbose_name="Edits Pending"),
                ),
                ("last_updated", models.DateTimeField(db_column="last_updated", verbose_name="Last Updated")),
                ("link_order", models.PositiveIntegerField(db_column="link_order", default=0)),
                ("recording_credit", models.TextField(db_column="entity0_credit", verbose_name="Recording Credit")),
                ("work_credit", models.TextField(db_column="entity1_credit", verbose_name="Work Credit")),
            ],
            options={
                "verbose_name_plural": "Recording Work Links",
                "db_table": "l_recording_work",
                "managed": False,
            },
        ),
    ]
