from django.urls import path
from . import views

urlpatterns = [
    path('coding/', views.coding),
    path('golf/', views.golf),
    # path('gallery/', views.gallery),
    path('art/', views.art),
    path('cultureNews/', views.cultureNews),
    path('news/', views.news),
    path('hsollc/', views.hsollc),
    path('', views.landing),
]
