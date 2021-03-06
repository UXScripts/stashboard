import logging
import os

logging.info("IMPORTING SETTINGS")

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from google.appengine.dist import use_library
try:
    use_library('django', '1.2')
except:
    pass

from django.conf import settings
_ = settings.TEMPLATE_DIRS

def webapp_add_wsgi_middleware(app):
    from google.appengine.ext.appstats import recording
    app = recording.appstats_wsgi_middleware(app)
    return app
