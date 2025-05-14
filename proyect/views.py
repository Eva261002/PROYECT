from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Ruta completa

def about(request):
    return render(request, 'proyect/about.html')

