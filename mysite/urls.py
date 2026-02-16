"""URL configuration for mysite project."""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('news.urls')),
    path('admin/', admin.site.urls),
]
