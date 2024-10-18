from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rules.urls')),  # Adjust to match your app's URL configuration
]
