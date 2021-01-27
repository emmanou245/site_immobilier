from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from backoffice.models import CategorieMaison
from backoffice.models import Commande
from backoffice.models import Maison
from backoffice.models import Requette
from backoffice.models import Message

# Create your views here.
def home(request):
    if not request.user.is_authenticated :
        return redirect('login')
    search = request.GET.get('Search')
    maisons = []
    print(search)
    commandes = Commande.objects.all()
    users = User.objects.all()
    if search == None:
        maisons = Maison.objects.all()
    else:
        maisons = Maison.objects.filter(quartier__icontains=search)
    print(Maison)

    control = {'commandes': commandes, 'users': users, 'maisons': maisons}
    return render(request,'index.html', control)


def inscrire(request):
    if request.user.is_authenticated :
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = User.objects.create_user(username,email,password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return redirect('login')
    return render(request, 'signup.html')

def connecter(request):
    if request.user.is_authenticated :
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password', '')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        return redirect('/')
    return render(request,'login.html')

def deconnecter(request):
    logout(request)
    return redirect('login')

def detail_maison(request,id_maison):
    maison = Maison.objects.get(id=id_maison)
    if request.method == 'POST':
        telephone = request.POST.get('telephone', '')
        message = request.POST.get('message','')
        commande = Commande()
        commande.message = message
        commande.telephone = telephone
        commande.maison = maison
        commande.user = request.user
        commande.save()
    return render(request, 'detail_maison.html', locals())

def appropos(request):
    return render(request, 'appropos.html')

def requette(request):
    liste_categories = CategorieMaison.objects.all()
    if request.method == 'POST':
        categorie_id = request.POST.get('categorie_id', '')
        nombre_chambre = request.POST.get('nombre_chambre', '')
        ville = request.POST.get('ville', '')
        quartier = request.POST.get('quartier', '')
        message = request.POST.get('message', '')
        telephone = request.POST.get('telephone', '')
        prix = request.POST.get('prix', '')
        requette = Requette()
        categorie = CategorieMaison.objects.get(id=categorie_id)
        requette.categorie = categorie
        requette.nombre_chambre = nombre_chambre
        requette.ville = ville
        requette.quartier = quartier
        requette.message = message
        requette.telephone = telephone
        requette.prix = prix
        requette.user = request.user
        requette.save()
        return redirect('/')
    return render(request, 'requette.html',locals())

def anonce(request):
    search = request.GET.get('Search')
    maisons = []
    print(search)
    messages = Message.objects.all()
    users = User.objects.all()
    if search == None:
        maisons = Maison.objects.all()
    else:
        maisons = Maison.objects.filter(quartier__icontains=search)
    print(Maison)
    if request.method == 'POST':
        telephone = request.POST.get('telephone', '')
        message = request.POST.get('message','')
        messag = Message()
        messag.message = message
        messag.telephone = telephone
        messag.user = request.user
        messag.save()

    context = {'messages': messages, 'users': users, 'maisons': maisons}
    return render(request, 'anonce.html', context)

def ajouter_maison(request):
    liste_categories = CategorieMaison.objects.all()
    if request.method == 'POST':
        categorie_id = request.POST.get('categorie_id', '')
        nombre_chambre = request.POST.get('nombre_chambre', '')
        photo = request.FILES.get('photo', '')
        description = request.POST.get('description', '')
        prix = request.POST.get('prix', '')
        quartier = request.POST.get('quartier', '')
        ville = request.POST.get('ville', '')
        depot_initial = request.POST.get('depot_initial','')
        caution = request.POST.get('caution','')
        disponibilite = request.POST.get('disponibilite', '')
        maison = Maison()
        categorie = CategorieMaison.objects.get(id=categorie_id)
        maison.categorie = categorie
        maison.nombre_chambre = nombre_chambre
        maison.photo = photo
        maison.description = description
        maison.prix = prix
        maison.quartier = quartier
        maison.ville = ville
        maison.depot_initial = depot_initial
        maison.caution = caution
        maison.disponibilite = disponibilite
        maison.user = request.user
        maison.save()
        return redirect('anonce')
    return render(request, 'ajouter_maison.html',locals())