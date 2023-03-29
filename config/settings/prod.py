from config.settings.base import *

CSRF_TRUSTED_ORIGINS = [f'https://{DOMAIN}', 'https://*.127.0.0.1']

if not DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

try:
    from config.settings.local import *
except ModuleNotFoundError:
    pass
