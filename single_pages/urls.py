from django.urls import path
from . import views

urlpatterns = [
    path('golf/', views.golf),
    path('art/', views.art),
    path('cultureNews/', views.cultureNews),
    path('hsollc/', views.hsollc),
    path('', views.landing),
]
