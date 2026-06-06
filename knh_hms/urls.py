from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.management import call_command
from django.contrib.auth import get_user_model

# Admin branding
admin.site.site_header = "Dr. Horton Dental Clinic Administration"
admin.site.site_title = "Dr. Horton Dental Clinic Portal"
admin.site.index_title = "Welcome to Dr. Horton Dental Clinic"

User = get_user_model()

# Temporary setup view – remove after first use
def setup_database(request):
    try:
        call_command('migrate', interactive=False)
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        return HttpResponse("✅ Database migrated and superuser created.<br>Login: admin / admin123<br>Remove this URL now!")
    except Exception as e:
        return HttpResponse(f"❌ Error: {e}")

urlpatterns = [
    # Temporary setup endpoint – REMOVE AFTER RUNNING
    path('setup/', setup_database),

    # Admin
    path('admin/', admin.site.urls),

    # Accounts (login, logout, registration)
    path('accounts/', include('accounts.urls')),

    # Other apps (uncomment if they have urls.py)
    path('appointments/', include('appointments.urls')),
    path('billing/', include('billing.urls')),
    path('patients/', include('patients.urls')),
    path('staff/', include('staff.urls')),
    path('pharmacy/', include('pharmacy.urls')),
    path('medical-records/', include('medical_records.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('reports/', include('reports.urls')),

    # Public landing page
    path('', TemplateView.as_view(template_name='landing.html'), name='landing'),
]