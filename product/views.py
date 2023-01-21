from django.shortcuts import render
from commande.models import Commande
from client.models import Client
from .models import Produit
from .models import Marque
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='acces')

def home(request):
    commandes=Commande.objects.all()
    clients=Client.objects.all()
    context={'commandes':commandes,'clients':clients}
    return render(request, 'produit/index.html',context)

def listproduit(request):
    produit=Produit.objects.all()
    context={'produit':produit}
    return render(request, 'produit/list_produit.html',context)

