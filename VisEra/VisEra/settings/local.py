
from .base import *

SECRET_KEY = '6zxwqb2702hopft*m4qx6cu106%ne0_ahc*6ln-ii0vz&+pu!s'
DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}

