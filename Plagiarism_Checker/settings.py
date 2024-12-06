"""
Django settings for Plagiarism_Checker project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os

from pathlib import Path

#import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


#django_heroku.settings(locals())


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Asegúrate de que BASE_DIR esté definido correctamente
]

# Nuevo codigo agregado 
MEDIA_URL = '/media/'  # URL pública para acceder a los archivos
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Ruta física en tu servidor


LOGIN_URL = '/login/'  # URL para la página de login
LOGIN_REDIRECT_URL = '/index/'  # Redirige después de iniciar sesión exitosamente
LOGOUT_REDIRECT_URL = '/login/'  # Redirige después de cerrar sesión


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jjhy1%zxbzl@z$oqh75zm+e(%-d7r-biy!2=_v1h^@zsn08=-8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ["127.0.0.1:8000"]

ALLOWED_HOSTS = ['localhost', '127.0.0.1', "plagioplagio-925018936781.us-central1.run.app"]

# Application definition

INSTALLED_APPS = [
    'plagiarismchecker.apps.PlagiarismcheckerConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Plagiarism_Checker.urls'

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

WSGI_APPLICATION = 'Plagiarism_Checker.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'plagioInspector',
        'ENFORCE_SCHEMA': False,  # MongoDB es esquemático flexible
        'CLIENT': {
            'host': 'mongodb+srv://Abimael:rkLggcGJ5aFjyxX@cluster0.vrdld.mongodb.net/plagioInspector?retryWrites=true&w=majority',  # Cambia según tu configuración
            'authMechanism': 'SCRAM-SHA-1',
        }
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Autenticación predeterminada
    'plagiarismchecker.backends.EmailAuthBackend',  # Autenticación por correo
]



# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

