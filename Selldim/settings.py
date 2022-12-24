from pathlib import Path
import os
from decouple import config
import django_heroku
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config('SECRET_KEY')


DEBUG = config('DEBUG', cast=bool)


ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'channels',

    'Selldim.accounts',
    'Selldim.products',
    'Selldim.common',
    'Selldim.chat',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "whitenoise.middleware.WhiteNoiseMiddleware",

    # 'whitenoise.middleware.WhiteNoiseMiddleware',
]


ROOT_URLCONF = 'Selldim.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]


WSGI_APPLICATION = 'Selldim.wsgi.application'


DATABASES = {

    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        'ENGINE': 'django.db.backends.postgresql',

        # 'NAME': 'Selldim',
        'NAME': 'd9ud0d8hr43v9v',

        # 'USER': 'postgres',
        'USER': 'yoostapgsollap',
        'PASSWORD': config('PASSWORD'),

        # 'HOST': 'localhost',
        'HOST': 'ec2-3-229-161-70.compute-1.amazonaws.com',

        # 'PORT': '5432',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators


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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#
# STATICFILES_DIRS = [
#     BASE_DIR / STATIC_URL
# ]


STATIC_URL = '/static/'
STATIC_ROOT = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]


# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


django_heroku.settings(locals())


MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


ASGI_APPLICATION = 'Selldim.asgi.application'


# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels.layers.InMemoryChannelLayer"
#     }
# }


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis-server-name", 6379)],
        },
    },
}


LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'login'






#TODO | Search bar!                                        // DONE! //
#TODO | Messages between users                             // DONE! //
#TODO | Like button (adding to favourites)                 // DONE! //
#TODO | User favourite page                                // DONE! //
#TODO | User Profile Picture                               // DONE! //
#TODO | Images to show while creating a new add            // DONE! //


#TODO | Hide secret key                                     // DONE //
#TODO | Add 404,404,500 page                                // DONE //
#TODO | Add JS pop up messages
#TODO | Add django admin groups                             // DONE //
#TODO | Fix current user no picture msg bug                 // DONE //
#TODO | Fix error product deleted crashes chat room         // DONE //