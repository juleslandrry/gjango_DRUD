from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='accueil'),
    path('listproduit',views.listproduit,name='listproduit'),
    path('ajoutproduit',views.ajoutproduit,name='ajoutproduit'),
    path('modifierproduit/<str:pk>',views.modifierproduit,name='modifierproduit'),
    path('supprimerproduit/<str:pk>',views.sup_produit,name='sup_produit')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)