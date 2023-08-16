from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('globus_portal_framework.urls')),
    path('', include('social_django.urls', namespace='social')),
]
