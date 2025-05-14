from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

def index(request):
    return render(request, 'notifications/index.html')

def list_demo(request):
    return render(request, 'notifications/list.html')
    
