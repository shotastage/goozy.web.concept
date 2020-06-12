import os
import sys

try:

    if "postgres://" in os.environ["DATABASE_URL"]:

        import dj_database_url

        database_setting = {
            'default': dj_database_url.config(default=os.environ["DATABASE_URL"])
        }
    else:
        database_setting = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': os.environ["GOOZY_DB_NAME"],
                'USER': os.environ["GOOZY_DB_USER"],
                'PASSWORD': os.environ["GOOZY_DB_PASS"],
                'HOST': os.environ["GOOZY_DB_HOST"],
                'PORT': '5432',
            }
        }
except BaseException:
    database_setting = {}
