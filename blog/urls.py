
# importamos la funcio path de Django y todas las vista de la app blog
from django.urls import path
from . import views

from django.conf.urls import url

#Agregamos los patrones de urls de la app 
# name='post_list' es el nombre de la URL que se utilizará para identificar a la vista. 
urlpatterns = [
    path('', views.post_list, name = 'post_list' ),
    path('post/<int:pk>/', views.post_detail, name = 'post_detail' ),
    path('post/new/', views.post_new, name = 'post_new' ),
    path('post/<int:pk>/edit', views.post_edit, name = 'post_edit' ),
    path('drafts/', views.post_draft_list, name = 'post_draft_list' ),
    path('post/<pk>/drafts/', views.post_publish, name = 'post_publish' ),
    path('post/<pk>/remove/', views.post_remove, name = 'post_remove' ),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),

]