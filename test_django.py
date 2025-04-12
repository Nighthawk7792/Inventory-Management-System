# test_django.py
import django
from django.conf import settings

if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY='temp-secret-key',
        ROOT_URLCONF=__name__,
        INSTALLED_APPS=['django.contrib.staticfiles'],
    )

from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("Django is working!")

urlpatterns = [path('', home)]

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(['test_django.py', 'runserver'])