"""
WSGI config for knh_hms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'knh_hms.settings')

# ONE‑TIME DATABASE SETUP (remove after first successful run)
from django.core.management import call_command
from django.db import connection
from django.contrib.auth import get_user_model

User = get_user_model()
try:
    # Check if the accounts_user table exists
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='accounts_user';")
        if not cursor.fetchone():
            call_command('migrate', verbosity=1, interactive=False)
            if not User.objects.filter(is_superuser=True).exists():
                User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            print("Database initialized and superuser created.")
        else:
            print("Database already initialized.")
except Exception as e:
    print(f"Setup error: {e}")

application = get_wsgi_application()