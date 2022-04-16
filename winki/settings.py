"""
Django settings for winki project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2j!s4$wxs^9o=sp0^lpr4)+z3jn-dwavlrm3yz(z-^r_ivglyd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['winki.com', '127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    # our apps
    'social_django',
    'django_extensions',
    'easy_thumbnails',
    'account.apps.AccountConfig',
    'images.apps.ImagesConfig',
    'actions.apps.ActionsConfig',
    
    # default apps
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

ROOT_URLCONF = 'winki.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'winki.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/site_statics/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets")
]

STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn", "static_root")

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "static_cdn", "media_root")


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'dashboard'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',        # authentication based on username and password
    'account.authentication.EmailAuthBackend',          # authentication based on email and password
    'social_core.backends.google.GoogleOAuth2',         # authentication with google
    'social_core.backends.instagram.InstagramOAuth2',   # authentication with instagram  
]


SOCIAL_AUTH_GOOGLE_OAUTH_KEY = '378588283371-2g2ui639abv306i0ld96993iff09fndb.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH_SECRET = '977uognuuw-yvc-AuseJWoeW'

SOCIAL_AUTH_INSTAGRAM_KEY = ''
SOCIAL_AUTH_INSTAGRAM_SECRET = ''


THUMBNAIL_DEBUG = True


from django.urls import reverse_lazy

ABSOLUTE_URL_OVERRIDES = {
'auth.user': lambda u: reverse_lazy('user_detail', args=[u.username])
}