from django.urls import path
from . import views

app_name = 'notifications'  
 
 
urlpatterns = [
    path('', views.index, name='index'),
   
    path('list/', views.list_demo, name='list'),
]