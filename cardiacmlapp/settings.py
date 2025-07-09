import os
from pathlib import Path
import dj_database_url
import django_heroku

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret-key')

# DEBUG = os.environ.get('DEBUG', 'False') == 'True'
DEBUG = True

# ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['denisjjuuko.pythonanywhere.com']
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'predictor',
    'cardiacmlapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # only once!
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cardiacmlapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cardiacmlapp.wsgi.application'

# Database (Heroku handles DATABASE_URL environment variable)
# DATABASES = {
#     'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd4ohk50v3d79ff',       # this is your database name
#         'USER': 'u2p9ehp2irf2e5',         # your PostgreSQL username
#         'PASSWORD': 'p3ea18abd4ff259aabeb01371691b5ae6f3ec0418c1f3364707e9ffb142226200',     # the password you set during installation
#         'HOST': 'cfls9h51f4i86c.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com',
#         'PORT': '5432',
#         'URL': 'postgres://u2p9ehp2irf2e5:p3ea18abd4ff259aabeb01371691b5ae6f3ec0418c1f3364707e9ffb142226200@cfls9h51f4i86c.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d4ohk50v3d79ff',
#         'Heroku CLI': 'heroku pg:psql postgresql-contoured-59105 --app mlcardio',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mlcardiodb',       # this is your database name
#         'USER': 'postgres',         # your PostgreSQL username
#         'PASSWORD': 'admin123',     # the password you set during installation
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': dj_database_url.config(default='postgres://user:password@localhost:5432/dbname')
# }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# STATIC_URL = '/static/'
STATIC_DIRS = [BASE_DIR / "static"]
# STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Heroku-specific settings
# django_heroku.settings(locals())
