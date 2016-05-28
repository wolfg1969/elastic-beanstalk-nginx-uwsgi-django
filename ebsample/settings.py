import environ
from base_settings import *

current = environ.Path(__file__)
root = current - 3  # three folder back (/a/b/c/ - 3 = /)
project_root = current - 2

env = environ.Env(DEBUG=(bool, False),)  # set default values and casting

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')  # False if not in os.environ

DATABASES = {
    'default': env.db(),
}

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

STATIC_ROOT = '/var/www/html'
STATIC_URL = '/static/'

print STATIC_ROOT
