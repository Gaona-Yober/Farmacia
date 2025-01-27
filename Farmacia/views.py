# views.py de tu aplicación
from django.shortcuts import render

def home(request):
    return render(request, 'inicio.html')
