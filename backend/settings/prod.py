""" Production Settings """

from .dev import *

############
# DATABASE #
############
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'korrixco_DB',
        'USER': 'korrixco_root',
        'PASSWORD': 'f=UQJ]H&s3Lq',
        'HOST': '174.136.12.174',
        'PORT': '3306',
    }
}

############
# SECURITY #
############

# DEBUG = bool(os.getenv('DJANGO_DEBUG', ''))

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', SECRET_KEY)

# Set to your Domain here (eg. 'django-vue-template-demo.herokuapp.com')
ALLOWED_HOSTS = ['*']
