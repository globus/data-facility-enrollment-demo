"""
Django settings for data_facility_enrollment_demo project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-wun@p3&1@di-7az!q98lr$3(2s8#-2pucgozxq^qxu+1zu(ka5"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

ARC_PROJECT_FILE = BASE_DIR / "data_facility_enrollment_demo/data/projects.json"
ARC_STORAGE_FILE = BASE_DIR / "data_facility_enrollment_demo/data/storage.json"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.postgres",
    "django.contrib.staticfiles",
    "data_facility_enrollment_demo",
    "globus_portal_framework",
    "social_django",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "globus_portal_framework.middleware.ExpiredTokenMiddleware",
    "globus_portal_framework.middleware.GlobusAuthExceptionMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
]

# Authentication backends setup OAuth2 handling and where user data should be
# stored
AUTHENTICATION_BACKENDS = [
    "globus_portal_framework.auth.GlobusOpenIdConnect",
    "django.contrib.auth.backends.ModelBackend",
]

ROOT_URLCONF = "data_facility_enrollment_demo.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "globus_portal_framework.context_processors.globals",
            ],
        },
    },
]

WSGI_APPLICATION = "data_facility_enrollment_demo.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "sqlite",
    }
}

# This is a general Django setting if views need to redirect to login
# https://docs.djangoproject.com/en/4.2/ref/settings/#login-url
LOGIN_URL = "/login/globus"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# This dictates which scopes will be requested on each user login
SOCIAL_AUTH_GLOBUS_SCOPE = [
    "openid",
    "profile",
    "email",
    "urn:globus:auth:scope:search.api.globus.org:all",
    "urn:globus:auth:scope:transfer.api.globus.org:all",
]

SOCIAL_AUTH_GLOBUS_KEY = "<redacted>"
SOCIAL_AUTH_GLOBUS_SECRET = "<redacted>`"
SEARCH_INDEX_UUID = '8c47de5e-a969-4912-abd5-c29130ae526e'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "stream": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {"handlers": ["stream"], "level": "INFO"},
        "django.db.backends": {"handlers": ["stream"], "level": "WARNING"},
        "globus_portal_framework": {"handlers": ["stream"], "level": "DEBUG"},
        "data_facility_enrollment_demo": {
            "handlers": ["stream"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_DIRS = [BASE_DIR / "staticfiles"]
STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"

try:
    from data_facility_enrollment_demo.local_settings import *
except ImportError:
    contents = """
        SOCIAL_AUTH_GLOBUS_KEY = "key"
        SOCIAL_AUTH_GLOBUS_SECRET = "secret"
    """
    print(
        f'Create a file next to your "settings.py" file with the following:\n\n {contents}'
    )
    raise Exception("Portal Start Failed, please resolve the auth errors first!")
