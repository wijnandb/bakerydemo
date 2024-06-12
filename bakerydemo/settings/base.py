"""
Django settings for temp project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os

import dj_database_url

# Build paths inside the project like this: os.path.join(PROJECT_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "c6u0-9c!7nilj_ysatsda0(f@e_2mws2f!6m0n^o*4#*q#kzp)"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Uncomment (and adjust as appropriate) to enable django-debug-toolbar
# INTERNAL_IPS = [
#     '127.0.0.1',
# ]

# Application definition

INSTALLED_APPS = [
    "bakerydemo.base",
    "bakerydemo.blog",
    "bakerydemo.breads",
    "bakerydemo.locations",
    "bakerydemo.recipes",
    "bakerydemo.search",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.api.v2",
    "wagtail.locales",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.routable_page",
    "wagtail.contrib.table_block",
    "wagtail.contrib.typed_table_block",
    "wagtail.contrib.search_promotions",
    "wagtail.contrib.settings",
    "wagtail.contrib.simple_translation",
    "wagtail.contrib.styleguide",
    "wagtail",
    "rest_framework",
    "modelcluster",
    "taggit",
    "wagtailfontawesomesvg",
    # Uncomment to enable django-debug-toolbar
    # "debug_toolbar",
    "django_extensions",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
]

MIDDLEWARE = [
    # Uncomment to enable django-debug-toolbar
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
ROOT_URLCONF = "bakerydemo.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            "bakerydemo/templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ],
        },
    },
]

WSGI_APPLICATION = "bakerydemo.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if "DATABASE_URL" in os.environ:
    DATABASES = {"default": dj_database_url.config(conn_max_age=500)}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "bakerydemodb"),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

STATIC_ROOT = os.path.join(PROJECT_DIR, "collect_static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(PROJECT_DIR, "media")
MEDIA_URL = "/media/"

# Override in local settings or replace with your own key. Please don't use our demo key in production!
GOOGLE_MAP_API_KEY = "AIzaSyD31CT9P9KxvNUJOwDq2kcFEIG8ADgaFgw"

# Use Elasticsearch as the search backend for extra performance and better search results
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
        "INDEX": "bakerydemo",
    },
}

# Wagtail settings
WAGTAIL_SITE_NAME = "bakerydemo"

WAGTAIL_I18N_ENABLED = True

WAGTAIL_CONTENT_LANGUAGES = LANGUAGES = [
    ("en", "English"),
    ("de", "Deutsch"),
    ("ar", "العربيّة"),
]

WAGTAILIMAGES_AVIF_QUALITY = 60

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "changeme")

# Content Security policy settings
# http://django-csp.readthedocs.io/en/latest/configuration.html

# Only enable CSP when enabled through environment variables.
if "CSP_DEFAULT_SRC" in os.environ:
    MIDDLEWARE.append("csp.middleware.CSPMiddleware")

    # Only report violations, don't enforce policy
    CSP_REPORT_ONLY = True

    # The “special” source values of 'self', 'unsafe-inline', 'unsafe-eval', and 'none' must be quoted!
    # e.g.: CSP_DEFAULT_SRC = "'self'" Without quotes they will not work as intended.

    CSP_DEFAULT_SRC = os.environ.get("CSP_DEFAULT_SRC").split(",")
    if "CSP_SCRIPT_SRC" in os.environ:
        CSP_SCRIPT_SRC = os.environ.get("CSP_SCRIPT_SRC").split(",")
    if "CSP_STYLE_SRC" in os.environ:
        CSP_STYLE_SRC = os.environ.get("CSP_STYLE_SRC").split(",")
    if "CSP_IMG_SRC" in os.environ:
        CSP_IMG_SRC = os.environ.get("CSP_IMG_SRC").split(",")
    if "CSP_CONNECT_SRC" in os.environ:
        CSP_CONNECT_SRC = os.environ.get("CSP_CONNECT_SRC").split(",")
    if "CSP_FONT_SRC" in os.environ:
        CSP_FONT_SRC = os.environ.get("CSP_FONT_SRC").split(",")
    if "CSP_BASE_URI" in os.environ:
        CSP_BASE_URI = os.environ.get("CSP_BASE_URI").split(",")
    if "CSP_OBJECT_SRC" in os.environ:
        CSP_OBJECT_SRC = os.environ.get("CSP_OBJECT_SRC").split(",")
