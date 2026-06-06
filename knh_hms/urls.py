from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.management import call_command
from django.contrib.auth import get_user_model

admin.site.site_header = "Dr. Horton Dental Clinic Administration"
admin.site.site_title = "Dr. Horton Dental Clinic Portal"
admin.site.index_title = "Welcome to Dr. Horton Dental Clinic"

User = get_user_model()

def setup(request):
    try:
        call_command('migrate', interactive=False)
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        return HttpResponse("✅ Setup complete. Use admin / admin123")
    except Exception as e:
        return HttpResponse(f"Error: {e}")

urlpatterns = [
    path('setup/', setup),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', TemplateView.as_view(template_name='landing.html'), name='landing'),
]