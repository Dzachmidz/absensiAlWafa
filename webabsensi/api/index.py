import os
import sys
import traceback
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'absensi.settings')

django_app = None
init_error = None

try:
    from django.core.wsgi import get_wsgi_application
    django_app = get_wsgi_application()
except Exception as e:
    init_error = traceback.format_exc()

def app(environ, start_response):
    if init_error:
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/plain; charset=utf-8')]
        start_response(status, headers)
        error_msg = f"Django WSGI Initialization Failed:\n\n{init_error}"
        return [error_msg.encode('utf-8')]
    
    return django_app(environ, start_response)

