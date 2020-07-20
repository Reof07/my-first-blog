
# importamos la funcio path de Django y todas las vista de la app blog
from django.urls import path
from . import views

#Agregamos los patrones de urls de la app 
# name='post_list' es el nombre de la URL que se utilizará para identificar a la vista. 
urlpatterns = [
    path('', views.post_list, name = 'post_list' ),
]