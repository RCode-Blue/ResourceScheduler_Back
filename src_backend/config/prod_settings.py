import os

SECRET_KEY = '5j_!%*1@aqyhn%%zff#l6n%4lecm_5*)jrsfd4$fmvzf=-)25u'
ALLOWED_HOSTS = ["https://serene-dusk-06086.herokuapp.com", "0.0.0.0", "localhost"]
DEBUG=False
# CSRF_COOKIE_SECURE = True

DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_USERNAME = os.environ["DB_USERNAME"]
DB_NAME = os.environ["DB_NAME"]

# Database
DATABASES = {
  "default":{
    "ENGINE": "django.db.backends.postgresql_psycopg2",
    "NAME": DB_NAME,
    "USER": DB_USERNAME,
    "PASSWORD": DB_PASSWORD,
    "HOST": "rosie.db.elephantsql.com",
    "PORT": "5432"
    }
}