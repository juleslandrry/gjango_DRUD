from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.list_commande, name='listcommande'),
    path('ajout_commande',views.ajouter_commande, name='ajout_commande'),
    path('modifier_commande/<str:pk>',views.modifier_command, name='modifier_commande'),
    path('supprimer_commande/<str:pk>',views.supprimer_command, name='supprimer_commande'),
    path('supprimer_commande/<str:pk>',views.supprimer_command, name='supprimer_commande')
]