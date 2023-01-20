from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='accueil'),
    path('listproduit',views.listproduit,name='listproduit')
]