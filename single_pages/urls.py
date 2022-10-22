from django.urls import path
from . import views

urlpatterns = [
    path('golf/', views.golf),
    path('art/', views.art),
    path('cultureheadline/', views.cultureheadline),
    path('hsollc/', views.hsollc),
    path('', views.landing),
]
