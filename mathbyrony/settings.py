"""
Django settings for mathbyrony project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qkikxb(s78)sct=x7!9!$()@mqm*v6-o@$+iq&nj*ykd)xgntt'
API_KEY_SECRET = 'mahmudul7959'
FCM_SERVER_KEY = 'AAAA9lV8u74:APA91bE-L_tirOl2DP0N9THg6_e3wbGGUa6xHSRGoC9-h9oU44pJrJMQ2MpguhQ-y2UVMKtyoV89oxU0J5bQ5LqYfLSNegYydkeAGB2n-nnIQtmafWSwTYX1gf8HyX8wKds5HZIPMYvq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SITE_DOMAIN = "http://ec2-3-14-65-191.us-east-2.compute.amazonaws.com"
SITE_DOMAIN = "http://127.0.0.1:8000"
# ALLOWED_HOSTS = ['ec2-3-14-65-191.us-east-2.compute.amazonaws.com',]
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #install apps
    'user_profile.apps.UserProfileConfig',
    'question.apps.QuestionConfig',
    'common.apps.CommonConfig',
    'notification.apps.NotificationConfig',
    'bigoto_bochor.apps.BigotoBochorConfig',
    'boi_porichiti.apps.BoiPorichitiConfig',
    'shop.apps.ShopConfig',
    'goniter_itihash.apps.GoniterItihashConfig',
    'blog.apps.BlogConfig',
    'topic_vittic_porashona.apps.TopicVitticPorashonaConfig',

    #install package apps
    'ckeditor',
    'ckeditor_uploader',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'corsheaders',
    'django_cleanup.apps.CleanupConfig',
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 25,
}

#CKEDITOR_UPLOAD_PATH
CKEDITOR_UPLOAD_PATH = "uploads/"

#CKEDITOR_CONFIGS
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'Preview',]},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            # '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',]},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image','Mathjax', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            # '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            # # '/',  # put this to force next toolbar on new line
            # {'name': 'yourcustomtools', 'items': [
            #     # put the name of your editor.ui.addButton here
            #     'Preview',
            #     'Maximize',

            # ]},
            {'name': 'about', 'items': ['About']},
        ],
        'toolbar': 'YourCustomToolbarConfig',
        'height': 200,
        'width': '100%',
        # 'filebrowserWindowHeight': 725,
        'filebrowserWindowWidth': 740,
        'toolbarCanCollapse': True,
        'mathJaxLib': 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'codesnippet',
            'image2',
            'mathjax',
            'iframe',
            'colordialog'
        ]),
    }
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mathbyrony.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR,],
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

WSGI_APPLICATION = 'mathbyrony.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

#For Hosting site
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'djangobackend',
#         'USER': 'mathbyrony',
#         'PASSWORD': 'mathbyronyawsdb',
#         'HOST': 'mathbyronydb.ckz96yxdewjh.us-east-2.rds.amazonaws.com',
#         'PORT': '3306',
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         },
#     }
# }

# #For Localhost
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mathbyrony_mysql',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

DATETIME_FORMAT = '%d-%m-%Y %H:%M:%S' 

USE_L10N = False

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "mathbyrony/static"),
]
STATIC_ROOT = os.path.join(BASE_DIR,'static')
#STATIC_ROOT = "/home/mahmudul7959/math-by-rony-backend-django/static"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
#MEDIA_ROOT = "/home/mahmudul7959/math-by-rony-backend-django/media"


CORS_ORIGIN_ALLOW_ALL = True

# # CORS_ORIGIN_WHITELIST
# CORS_ORIGIN_WHITELIST = [
#     "http://localhost:3000",
# ]