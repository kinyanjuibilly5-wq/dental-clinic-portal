from django.http import HttpResponse
from django.core.management import call_command
from django.contrib.auth import get_user_model

User = get_user_model()

def setup_database(request):
    try:
        # Run migrations
        call_command('migrate', interactive=False)
        # Create superuser if none exists
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        return HttpResponse("✅ Database migrated and superuser created.<br>Login: admin / admin123<br>Remove this URL now!")
    except Exception as e:
        return HttpResponse(f"❌ Error: {e}")

urlpatterns = [
    # ... your existing paths
    path('setup/', setup_database),   # <-- add this line
]