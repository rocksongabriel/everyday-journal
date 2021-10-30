from .base import *

DEBUG = True

SECRET_KEY = "9bbo9tlf+k)ar9*g^+#j7l)z=1x#w$5fxmvkj#47w=yrls&*pm"

INSTALLED_APPS += [
    "django_extensions",
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000'
]
