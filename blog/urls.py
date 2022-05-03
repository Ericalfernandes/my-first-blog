from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #caminho, view, e nome da url
    path('post/new/', views.post_new, name='post_new'), 
    path('post/edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('comment/', views.comment, name='comments'), #tentativa de exibir um html só com comentários de um post
]   