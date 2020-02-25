import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = os.urandom(24)
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
DEBUG = True

AUTH_PASSWORD_VALIDATORS = []
# CSRF_COOKIE_SECURE = False

# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'combineddjangoreact',
#         'USER': 'dev',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}