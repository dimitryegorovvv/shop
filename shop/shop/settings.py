"""
Django settings for shop project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = ''
MEDIA_ROOT = os.path.join(BASE_DIR, '')

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# MEDIA_URL = '/photos/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'photos')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=%podqk0^0v8#f!(qu5o8%y!8xwb1=b)fm#ob0#gwc8#^dp&rb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'payments',
    'users',
    'registration',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'add_goods',
    'anymail',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'users.middleware.YandexUserMiddleware',
    # 'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'social_django.context_processors.backends',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CART_SESSION_ID = 'cart'

# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# 2e586c345868b077059b7c34a4b16a8a-623e10c8-567c0a25

EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
ANYMAIL = {
    'MAILGUN_API_KEY': '2e586c345868b077059b7c34a4b16a8a-623e10c8-567c0a25',
    'MAILGUN_SENDER_DOMAIN': 'sandboxef238b9dfec3470cb5ca1444d2ac0ae5.mailgun.org',
}

DEFAULT_FROM_EMAIL = 'postmaster@sandboxef238b9dfec3470cb5ca1444d2ac0ae5.mailgun.org'

ACCOUNT_ACTIVATION_DAYS = 1

ACCOUNT_ACTIVATION_REQUIRED = False
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
REGISTRATION_AUTO_LOGIN = True 
REGISTRATION_OPEN = True 

AUTH_USER_MODEL = 'users.CustomUser'
REGISTRATION_FORM = 'users.forms.CustomUserCreationForm'

# AUTHENTICATION_BACKENDS = (
#     'social_core.backends.yandex.YandexOAuth2',
#     'django.contrib.auth.backends.ModelBackend',
# )

SESSION_COOKIE_AGE = 365 * 24 * 60 * 60

# ALLOWED_HOSTS = ["d28f-178-120-67-229.ngrok-free.app", '127.0.0.1', 'localhost']
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://c0b3-178-120-22-52.ngrok-free.app']

# SOCIAL_AUTH_YANDEX_OAUTH2_KEY = '5f7d4dec0c084cb380daadfdf7e2771e'
# SOCIAL_AUTH_YANDEX_OAUTH2_SECRET = '9d2b3025b19540a89940aa1c5ef9792e'

# # URL перенаправления после успешной аутентификации
# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/'
