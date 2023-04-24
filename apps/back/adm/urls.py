from django.contrib import admin
from django.urls import path
from apps.back.adm.views import adm

urlpatterns = [
    path('adm/', adm),
]
