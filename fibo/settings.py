
from django.core.exceptions import ImproperlyConfigured

import json
import os

CONFIGURATION_FILE = os.environ.get('FIBO_CONFIG')

if CONFIGURATION_FILE is None:
    raise ImproperlyConfigured(
        "ImproperlyConfigured: Set CONFIG environment variable"
    )


with open(CONFIGURATION_FILE) as f:
    configs = json.loads(f.read())


def get_env_var(setting, configs=configs):
    try:
        return configs[setting]
    except KeyError:
        raise ImproperlyConfigured(
            "ImproperlyConfigured: Set {0} environment variable".format(
                setting)
        )


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = get_env_var('DEBUG')

STATIC_URL = '/static/'

SECRET_KEY = get_env_var('SECRET_KEY')

ALLOWED_HOSTS = get_env_var('ALLOWED_HOSTS').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'core'
]

if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
else:
    STATIC_ROOT = "static"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'fibo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'core/templates')
        ],
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

WSGI_APPLICATION = 'fibo.wsgi.application'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR + '/media'

DATABASES = {
    'default': get_env_var('DATABASE_CONFIG')
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',   # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',   # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',   # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',   # noqa
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True
