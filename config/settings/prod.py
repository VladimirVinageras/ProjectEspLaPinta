from .base import *

import json

from django.core.exceptions import ImproperlyConfigured

# JSON-based secrets module
with open(os.path.join(BASE_DIR, 'secrets.json')) as f:
	secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
	'''Get the secret variable or return explicit exception.'''
	try:
		return secrets[setting]
	except KeyError:
		error_msg = 'Set the {0} environment variable'.format(setting)
		raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']

# Static Files

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Email Backend

EMAIL_HOST = 'mail.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Google ReCaptcha

RECAPTCHA_SECRET_KEY = get_secret('RECAPTCHA_SECRET_KEY')
RECAPTCHA_SITE_KEY = get_secret('RECAPTCHA_SITE_KEY')

# 2018.10.24-DEA
