from django.core.exceptions import ImproperlyConfigured
try:
    from .local import *  # noqa
except ImportError:
    from .default import *  # noqa