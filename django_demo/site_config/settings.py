"""
Django settings for the local lightweight demo.

This configuration is intentionally minimal and local-only.
It supports a read-only Django interface layer over already
generated forecasting / diagnostics demo artifacts.
"""

from pathlib import Path


# ---------------------------------------------------------
# Core paths
# ---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Repository root (one level above django_demo/)
REPO_ROOT = BASE_DIR.parent

# Local read-only demo artifacts
DEMO_ARTIFACT_DIR = REPO_ROOT / "data" / "processed" / "demo"


# ---------------------------------------------------------
# Local development settings
# ---------------------------------------------------------
SECRET_KEY = "django-local-demo-only-not-for-production"

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


# ---------------------------------------------------------
# Application definition
# ---------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "demo_ui",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "site_config.urls"


# ---------------------------------------------------------
# Templates
# ---------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "site_config.wsgi.application"


# ---------------------------------------------------------
# Database
# ---------------------------------------------------------
# Default local SQLite database.
# The demo is read-only with respect to forecasting artifacts,
# but Django may still use sqlite3 for framework-level needs.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ---------------------------------------------------------
# Password validation
# ---------------------------------------------------------
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


# ---------------------------------------------------------
# Internationalization
# ---------------------------------------------------------
LANGUAGE_CODE = "el"

TIME_ZONE = "Europe/Athens"

USE_I18N = True
USE_TZ = True


# ---------------------------------------------------------
# Static files
# ---------------------------------------------------------
STATIC_URL = "static/"


# ---------------------------------------------------------
# Django defaults
# ---------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"