from django.shortcuts import render,redirect
from commande.models import Commande
from client.models import Client
from .models import Produit
from .models import Marque
from django.contrib.auth.decorators import login_required

import product
from .forms import ProduitForm

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

def ajoutproduit(request):
    form=ProduitForm()
    if request.method=='POST':
        form=ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listproduit')
    context={'form':form}
    return render (request ,'produit/ajouter_produit.html' , context)

def modifierproduit(request,pk):
    produit=Produit.objects.get(id=pk)
    form=ProduitForm(instance=produit)
    if request.method=='POST':
        form=ProduitForm(request.POST,instance=produit)
        if form.is_valid():
            form.save()
            return redirect('listproduit')
    context={'form':form}
    return render(request, 'produit/ajouter_produit.html', context)

def sup_produit(request,pk):
    produit=Produit.objects.get(id=pk)
    if request.method=='POST':
        produit.delete()
        return redirect('listproduit')
    context={'item':produit}
    return render(request, 'produit/sup_produit.html', context)