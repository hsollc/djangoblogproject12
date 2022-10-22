from django.urls import path
from django.urls import re_path as url
from . import views

urlpatterns = [
    path('golf/', views.golf),
    path('art/', views.art),
    path('hsollc/', views.hsollc),
    path('', views.landing),
]
