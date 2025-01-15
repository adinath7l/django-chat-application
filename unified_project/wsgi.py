# unified_project/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

# Change 'unified_project' to your project name if it is different.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unified_project.settings')

application = get_wsgi_application()
