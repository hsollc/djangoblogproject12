from django.urls import path
from django.conf.urls import include
from django.urls import re_path
from . import views

urlpatterns = [
    path('golf/', views.golf),
    path('art/', views.art),
    path('hsollc/', views.hsollc),
    path('', views.landing),
]
