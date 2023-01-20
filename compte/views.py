from email import message
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreerUtilisateur
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def inscriptionPage (request):
    form=CreerUtilisateur()
    if request.method=='POST':
        form=CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Creation de compte reussie pour '+user)
            return redirect('acces')
    context={'form':form}
    return render(request,'compte/inscription.html',context)


def accesPage (request):
    context={}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('accueil')
        else:
            messages.info(request,"Nom utilistaeur et/ou mot de pass invalide")
    return render(request,'compte/acces.html',context)

def logoutUser (request):
    logout(request)
    return redirect('acces')
