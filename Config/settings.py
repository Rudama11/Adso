from pathlib import Path
from django.contrib.messages import constants as messages
import os

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    messages.SUCCESS: 'success',
}

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-l$w2&3)pz0=h_a-hg^=k8%-ehfi2elsgexc&01&002-8rc@&al'

DEBUG = False

ALLOWED_HOSTS = ["conaldexboyaca.sogamosotecnologiadigital.pro"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app.apps.AppConfig',
    #dash
    'dashboard',
    #Index
    'inicio',
    #Login 
    'login',
    #lib
    'widget_tweaks',
    'django_select2',
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

ROOT_URLCONF = 'Config.urls'

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

WSGI_APPLICATION = 'Config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database-conaldex',
        'USER': 'user-conaldex',
        'PASSWORD': 'KH5J8DEiRBkz17RGr1fQ',
        'HOST': 'localhost',
        'PORT': '3306',
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

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Configuración de archivos estáticos
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Agregar la ruta del directorio de backups
BACKUP_ROOT = os.path.join(BASE_DIR, 'backups')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'app/static'),  # Ruta al directorio static principal
    os.path.join(BASE_DIR, 'app/static/node_modules'),  # Ruta al directorio node_modules
    ('backups', BACKUP_ROOT),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/dashboard'

#Tiempo para el correo
PASSWORD_RESET_TIMEOUT=1800

#inicio,# Olvido su contraseña
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'boyacaconaldex@gmail.com'
EMAIL_HOST_PASSWORD = 'ewfh mhlu txgs cnls'

AUTH_USER_MODEL = 'app.CustomUser'  # Cambia 'app' por el nombre de tu aplicación