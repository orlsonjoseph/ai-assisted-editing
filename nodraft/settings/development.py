from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Security configuration
# https://docs.djangoproject.com/en/3.2/topics/security/

CSRF_COOKIE_SECURE = False

SESSION_COOKIE_SECURE = False

SECRET_KEY = "django"

# Hosts configuration
# https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts

INTERNAL_IPS = ["127.0.0.1", "nodraft.local"]

ALLOWED_HOSTS = INTERNAL_IPS

# Miscellaneous

AGGREGATION_THRESHOLD = 10
