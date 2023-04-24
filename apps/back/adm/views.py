from django.shortcuts import render, redirect
from django.contrib import messages

def adm(request):
    return render(request, 'back/adm/adm.html')

