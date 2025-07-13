from django.urls import path
from . import views

app_name = 'books'  # Namespace para las URLs
 
urlpatterns = [
    path('', views.index, name='index'),
     path('books/list/', views.book_list, name='list'),
    path('books/detail/<int:book_id>/', views.book_detail, name='detail'),
     path('search/', views.book_search, name='search'),
] 