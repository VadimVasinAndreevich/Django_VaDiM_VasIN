from django.urls import path
from . import views

urlpatterns = [
    path('', views.links, name='links'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
]
