from django.conf import settings
from django.urls import path
from str.settings import STATIC_ROOT, STATIC_URL
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('contacto', views.contacto, name='contacto'),
    path('post/<pk>/delete/', views.post_delete, name='post_delete'),
    path('consulta', views.consulta, name='consulta'),
]
