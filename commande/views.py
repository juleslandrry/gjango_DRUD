from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

import commande
from .forms import CommandeForm
from .models import Commande
from .models import Client

# Create your views here.
@login_required(login_url='acces')
def list_commande (request):
    commandes=Commande.objects.all()
    clients=Client.objects.all()
    context={'commandes':commandes,'clients':clients}
    return render (request, 'commande/liste_commande.html',context)

@login_required(login_url='acces')
def ajouter_commande(request):
    form=CommandeForm()
    if request.method=='POST':
        form=CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listcommande')
    context={'form':form}
    return render (request, 'commande/ajouter_commande.html', context) 
    

@login_required(login_url='acces')
def modifier_command(request,pk):
    commande=Commande.objects.get(id=pk)
    form=CommandeForm(instance=commande)
    if request.method=='POST':
        form=CommandeForm(request.POST,instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render (request, 'commande/ajouter_commande.html', context)


@login_required(login_url='acces')
def supprimer_command (request,pk):
    commande=Commande.objects.get(id=pk)
    if request.method=='POST':
        commande.delete()
        return redirect('/')
    context={'item':commande}
    return render (request, 'commande/supprimer.html',context)