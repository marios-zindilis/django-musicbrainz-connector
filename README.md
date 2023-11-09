# Django MusicBrainz Connector #

The **Django MusicBrainz Connector** is a Django app that connects to a replica of the MusicBrainz database.

## Installation

1.  Install this module from [PyPI](https://pypi.org/):

    ```
    pip install django-musicbrainz-connector
    ```

    Alternatively, you can install from code with:

    ```
    git clone git@github.com:marios-zindilis/django-musicbrainz-connector.git
    cd django-musicbrainz-connector.git
    python setup.py sdist
    python -m pip install dist/django-musicbrainz-connector-0.0.1.tar.gz
    ```

2.  Append the app to your Django project's `settings.py` list of `INSTALLED_APPS`, for example:

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django_musicbrainz_connector',  # <--
    ]
    ```

3.  Create a read-only user in the MusicBrainz Postgresql replica database:

    ```sql
    \c musicbrainz_db
    CREATE USER django_musicbrainz_connector WITH PASSWORD 'sUp3rSecr3t';
    GRANT CONNECT ON DATABASE musicbrainz_db TO django_musicbrainz_connector;
    GRANT USAGE ON SCHEMA musicbrainz TO django_musicbrainz_connector;
    GRANT SELECT ON ALL TABLES IN SCHEMA musicbrainz TO django_musicbrainz_connector;
    ALTER USER django_musicbrainz_connector SET SEARCH_PATH TO musicbrainz;
    ```

    You can confirm this with something like:

    ```sql
    SELECT grantee, privilege_type FROM information_schema.role_table_grants WHERE table_name='area_type';
    ```

    The output should include the user you just created:

    ```
              grantee            | privilege_type
    ------------------------------+----------------
    musicbrainz                  | INSERT
    musicbrainz                  | SELECT
    musicbrainz                  | UPDATE
    musicbrainz                  | DELETE
    musicbrainz                  | TRUNCATE
    musicbrainz                  | REFERENCES
    musicbrainz                  | TRIGGER
    django_musicbrainz_connector | SELECT
    ```

    You can also connect to the database with `psql`:

    ```
    psql -d musicbrainz_db -U django_musicbrainz_connector
    SELECT * FROM musicbrainz.area_type;
    ```

4.  Add the MusicBrainz database to your Django project's `settings.py` list of `DATABASES`. You shouldn't use the
    MusicBrainz database as the Django default database, because this app is only mean to have read access. For example:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        },
        'musicbrainz_db': {
            'NAME': "musicbrainz_db",
            "ENGINE": "django.db.backends.postgresql",
            "USER": "django_musicbrainz_connector",
            "PASSWORD": "sUp3rSecr3t",
        },
    }
    ```

5.  Add the database router to your Django project's `settings.py` list of `DATABASE_ROUTERS`, for example:

    ```python
    DATABASE_ROUTERS = [
        "django_musicbrainz_connector.routers.DjangoMusicBrainzConnectorDatabaseRouter",
    ]
    ```

6.  Apply the migrations. This doesn't make any changes to the MusicBrainz database:

    ```
    python manage.py migrate
    ```

## Notes on Read-Only Access

This app provides read-only connectivity to the database, because it assumes that you maintain a replica of the
MusicBrainz Postgresql database, and therefore it makes no sense to be able to write to it. This is done in several
ways:

1.  It is recommended that you create a read-only user in Postgresql, and use that user for this app. The installation
    documentation includes step-by-step instructions for this.

2.  All models have `Meta.managed` set to `False`.

3.  For models registered in the Django Admin, methods `has_change_permission` and `has_delete_permission` are always
    set to `False`.
