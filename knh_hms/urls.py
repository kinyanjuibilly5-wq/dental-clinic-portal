from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView   # <-- add this

# Custom admin branding
admin.site.site_header = "Dr. Horton Dental Clinic Administration"
admin.site.site_title = "Dr. Horton Dental Clinic Portal"
admin.site.index_title = "Welcome to Dr. Horton Dental Clinic"

urlpatterns = [
    path('', TemplateView.as_view(template_name='landing.html'), name='landing'),  # <-- changed
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    # ... other paths (appointments, billing, etc.)
]