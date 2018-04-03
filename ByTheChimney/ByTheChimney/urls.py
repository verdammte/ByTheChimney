"""
Definition of urls for ByTheChimney.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('web_app.urls')),
    path('admin/', admin.site.urls),
]
