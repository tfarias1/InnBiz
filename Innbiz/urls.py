from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.front.website.urls')),
    path('', include('apps.back.adm.urls')),
]
