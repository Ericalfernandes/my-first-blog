from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'index'),
    path('post_list/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #caminho, view, e nome da url
    path('post/new/', views.post_new, name='post_new'), 
    path('post/newpost/', views.form_postnew, name='form_postnew'),
    path('post/edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('comment/', views.comment, name='comments'), #tentativa de exibir um html só com comentários de um post
]   