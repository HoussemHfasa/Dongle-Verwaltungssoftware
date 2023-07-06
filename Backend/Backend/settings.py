import os
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv

# Laden der Umgebungsvariablen
load_dotenv()

# Django Einstellungen
SECRET_KEY = 'django-insecure-94j33)2i@&eg%yxah@)4e1x-)87^cnr0c=&tqn41m3+5e3&s9p'
DEBUG = True
ALLOWED_HOSTS = []

# Installierte Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'User_loggin',
    'rest_framework',
    'rest_framework_simplejwt',
    'homepage',
    'benachrichtigung',
    'Lizenzseite',
    'corsheaders',
    'Adminseite',
    'Dongle_hinzufügen',
    'Lizenzhinzufügen',
    'LizenzAnfordern',
    'DongleAnfordern',

]

# Middleware Einstellungen
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

# CORS Einstellungen
CORS_ALLOW_ALL_ORIGINS = True
ROOT_URLCONF = 'Backend.urls'
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
]

# Template Einstellungen
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

# WSGI-Anwendung
WSGI_APPLICATION = 'Backend.wsgi.application'

# Datenbank Einstellungen
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

# Passwort-Validierung
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Benutzermodell
AUTH_USER_MODEL = 'User_loggin.CustomUser'
SILENCED_SYSTEM_CHECKS = ["auth.E403"]

# Sprache und Zeitzone
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Standard Auto-Feld
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework Einstellungen
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
         'rest_framework.authentication.BasicAuthentication',
    )
}

# Celery Einstellungen
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_TIMEZONE = 'Europe/Berlin'
CELERY_BEAT_SCHEDULE = {
    'check-lizenzen-ablauf': {
        'task': 'benachrichtigung.tasks.check_lizenzen_ablauf_task',
        'schedule': timedelta(days=1),
    },
}

# E-Mail Einstellungen
EMAIL_HOST = 'smtp-relay.sendinblue.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'Rama.Abazied@Student.HTW-Berlin.de'
EMAIL_HOST_PASSWORD = 'rWU3K2OhYvfmNI8F'

# Statische Dateien
STATIC_URL = '/static/'

# Authentifizierung-Backends
AUTHENTICATION_BACKENDS = [
    'User_loggin.backends.CustomUserModelAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]

SESSION_ENGINE = 'django.contrib.sessions.backends.db'