import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'groceryhub.settings')

# Auto-setup on cold start
django.setup()

try:
    from django.core.management import call_command
    call_command('migrate', '--run-syncdb', verbosity=0)
    call_command('collectstatic', '--noinput', verbosity=0)
    call_command('seed_store', verbosity=0)
except Exception as e:
    print(f"Setup warning: {e}")

app = get_wsgi_application()
