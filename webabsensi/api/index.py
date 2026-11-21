import os
import sys
import traceback
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'absensi.settings')

from django.core.wsgi import get_wsgi_application

try:
    _django_app = get_wsgi_application()
except Exception:
    _django_app = None
    _startup_error = traceback.format_exc()
else:
    _startup_error = None

# Vercel looks for 'app' or 'handler'
def handler(environ, start_response):
    if _startup_error:
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/plain; charset=utf-8')]
        start_response(status, headers)
        return [f"Startup Error:\n\n{_startup_error}".encode('utf-8')]
    
    try:
        return _django_app(environ, start_response)
    except Exception:
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/plain; charset=utf-8')]
        start_response(status, headers)
        return [f"Runtime Request Error:\n\n{traceback.format_exc()}".encode('utf-8')]

app = handler


