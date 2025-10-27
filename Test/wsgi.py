"""
WSGI config for Test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Test.settings")

application = get_wsgi_application()

try:
    from whitenoise import WhiteNoise
    import os as _os
    static_root = _os.path.join(_os.path.dirname(_os.path.dirname(__file__)), "static")
    application = WhiteNoise(application, root=static_root)
except Exception:
    # whitenoise absent — on continue sans optimisation static
    pass
