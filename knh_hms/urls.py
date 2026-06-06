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

# Temporary setup endpoint (remove after using)
def setup_database(request):
    try:
        call_command('migrate', interactive=False)
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        return HttpResponse("✅ Database ready.<br>Superuser: admin / admin123<br>Now remove this setup URL.")
    except Exception as e:
        return HttpResponse(f"❌ Error: {e}")

urlpatterns = [
    # Setup endpoint – run once, then remove this line
    path('setup/', setup_database),

    # Admin panel
    path('admin/', admin.site.urls),

    # Accounts (login, logout, register)
    path('accounts/', include('accounts.urls')),

    # Other apps – COMMENTED OUT because their urls.py files are missing
    # Uncomment only after you create the corresponding app/urls.py
    # path('appointments/', include('appointments.urls')),
    # path('billing/', include('billing.urls')),
    # path('patients/', include('patients.urls')),
    # path('staff/', include('staff.urls')),
    # path('pharmacy/', include('pharmacy.urls')),
    # path('medical-records/', include('medical_records.urls')),
    # path('dashboard/', include('dashboard.urls')),
    # path('reports/', include('reports.urls')),

    # Public landing page
    path('', TemplateView.as_view(template_name='landing.html'), name='landing'),
]