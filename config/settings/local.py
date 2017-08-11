from .base import *

DEBUG = env.bool('DJANGO_DEBUG', default=True)

SECRET_KEY = env('DJANGO_SECRET_KEY', default='r(@b1^eo8a5h5m7my_=g_=sx1yw&tyop7*wy5$u$qkdsci_)yr')

# JWT_AUTH['JWT_SECRET_KEY'] = SECRET_KEY