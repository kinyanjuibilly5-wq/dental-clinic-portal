from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. Django is working!")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
]