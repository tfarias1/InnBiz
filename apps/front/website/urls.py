from django.contrib import admin
from django.urls import path
from apps.front.website.views import index


urlpatterns = [
    path('', index, name='index'),
]
