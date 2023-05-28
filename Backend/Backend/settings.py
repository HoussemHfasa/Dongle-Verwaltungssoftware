import os
from datetime import timedelta
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-94j33)2i@&eg%yxah@)4e1x-)87^cnr0c=&tqn41m3+5e3&s9p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
<<<<<<< HEAD
    # 'django.contrib.staticfiles',
=======
    'django.contrib.staticfiles',
>>>>>>> Houssem
    'User_loggin',
    'rest_framework',
    'rest_framework_simplejwt',
    'homepage',
<<<<<<< HEAD
    'benachrichtigung',
    'Lizenzseite',
    
=======
    'corsheaders',

>>>>>>> Houssem

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
<<<<<<< HEAD
]
CORS_ALLOW_ALL_ORIGINS = True
=======
    'django.middleware.common.CommonMiddleware',
]
CORS_ALLOW_ALL_ORIGINS = True


>>>>>>> Houssem
ROOT_URLCONF = 'Backend.urls'
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",  # Replace with the address of your React frontend
]

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

WSGI_APPLICATION = 'Backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
        'OPTIONS': {
            'autocommit': True,
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
<<<<<<< HEAD
=======
AUTH_USER_MODEL = 'User_loggin.CustomUser'
SILENCED_SYSTEM_CHECKS = ["auth.E403"]
>>>>>>> Houssem

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

<<<<<<< HEAD
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_TIMEZONE = 'Europe/Berlin'
CELERY_BEAT_SCHEDULE = {
    'check-lizenzen-ablauf': {
        'task': 'benachrichtigung.tasks.check_lizenzen_ablauf_task',
        'schedule': timedelta(days=1),
    },
}
# SMTP-Konfiguration für Sendinblue
EMAIL_HOST = 'smtp-relay.sendinblue.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'Rama.Abazied@Student.HTW-Berlin.de'
EMAIL_HOST_PASSWORD = 'rWU3K2OhYvfmNI8F'
=======
STATIC_URL = '/static/'


AUTHENTICATION_BACKENDS = [
    'User_loggin.backends.CustomUserModelAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]
>>>>>>> Houssem
