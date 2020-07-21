
# importamos la funcio path de Django y todas las vista de la app blog
from django.urls import path
from . import views

#Agregamos los patrones de urls de la app 
# name='post_list' es el nombre de la URL que se utilizará para identificar a la vista. 
urlpatterns = [
    path('', views.post_list, name = 'post_list' ),
    path('post/<int:pk>/', views.post_detail, name = 'post_detail' ),
    path('post/new/', views.post_new, name = 'post_new' ),
    path('post/<int:pk>/edit', views.post_edit, name = 'post_edit' ),
]