import environ
from base_settings import *

current = environ.Path(__file__)
root = current - 3  # three folder back (/a/b/c/ - 3 = /)
project_root = current - 2

env = environ.Env(
    DEBUG=(bool, DEBUG),
    SECRET_KEY=(str, SECRET_KEY),
    ALLOWED_HOSTS=(list, ALLOWED_HOSTS),
)  # set default values and casting

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

INSTALLED_APPS = [
    'grappelli',
    'ebsample_app',
] + INSTALLED_APPS

DATABASES = {
    'default': env.db(),
}

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

STATIC_ROOT = project_root('static')

GRAPPELLI_ADMIN_TITLE = 'Django Sample Project'
