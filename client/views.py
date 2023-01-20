from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Client
from commande.filtre import CommandeFiltre
from django.contrib.auth.decorators import login_required

import client
from .forms_client import ClientForm
from .models import Client

# Create your views here.
@login_required(login_url='acces')
def list_client (request,pk):
    client=Client.objects.get(id=pk)
    commande=client.commande_set.all()
    commande_total=commande.count()
    myFilter=CommandeFiltre(request.GET,queryset=commande)
    commande=myFilter.qs
    context={'client':client,'commande':commande, 'commande_total':commande_total, 'myFilter':myFilter}
    return render(request, 'client/liste_client.html',context)

def ajout_client (request):
    form=ClientForm
    if request.method=='POST':
        form=ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'client/ajout_client.html', context)

def modifier_client (request,pk):
    client=Client.objects.get(id=pk)
    form=ClientForm(instance=client)
    if request.method=='POST':
        form=ClientForm(request.POST,instance=client)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render (request, 'client/ajout_client.html', context)

def supprimer_client (request,pk):
    client=Client.objects.get(id=pk)
    if request.method=='POST':
        client.delete()
        return redirect('/')
    context={'item':client}
    return render(request, 'client/supprimer_client.html', context)
    