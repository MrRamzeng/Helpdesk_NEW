import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '8qv#3dgy^9m%o)=2sikp$ld1s84r(yq^1@y^f(^3r1if=@39$n'

DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'help.Account'

INSTALLED_APPS = [
    'help',
    'ckeditor',
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

ROOT_URLCONF = 'Helpdesk.urls'

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

WSGI_APPLICATION = 'Helpdesk.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = 'ru-ru'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = False

TIME_INPUT_FORMATS = ['%H:%M']

DATE_INPUT_FORMATS = ['%d.%m.%Y']

DATETIME_FORMAT = '%d.%m.%Y %H:%M'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar':[
            ['Format',
                'Styles',
                'FontSize',
                '-',
                'Find',
                '-',
                'TextColor',
                '-',
                'Bold', 
                'Italic',
                'Underline',
                'CodeSnippet',
                '-',
                'NumberedList', 
                'BulletedList',
                '-',
                "Indent",
                "Outdent",
                '=',
                'JustifyLeft', 
                'JustifyCenter', 
                'JustifyRight', 
                'JustifyBlock', 
                '-',
                'Image', 
                'Table',
                'SpecialChar',
                '-', 
                'Preview']],
        'removePlugins': 'stylesheetparser',
        'extraPlugins': 'codesnippet',
        'width': 'auto'
    },
}

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = 'uploads/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'myfriends', 'static'),)
