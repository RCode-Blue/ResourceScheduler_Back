import os
import psycopg2

SECRET_KEY = os.urandom(24)
ALLOWED_HOSTS = ["https://serene-dusk-06086.herokuapp.com", "0.0.0.0", "localhost", "127.0.0.1"]
DEBUG = False
# CSRF_COOKIE_SECURE = True

DB_URL      = os.environ["DB_URL"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_USERNAME = os.environ["DB_USERNAME"]
DB_NAME     = os.environ["DB_NAME"]
DB_HOST     = os.environ["DB_HOST"]


# Database
DATABASES = {
  "default":{
    "ENGINE": "django.db.backends.postgresql_psycopg2",
    "NAME": DB_NAME,
    "USER": DB_USERNAME,
    "PASSWORD": DB_PASSWORD,
    "HOST": DB_HOST,
    "PORT": "5432"
    }
}

