from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from backoffice.models import CategorieMaison
from backoffice.models import Commande
from backoffice.models import Maison
from backoffice.models import Requette
from backoffice.models import Message
from backoffice.models import Images
import folium

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
        maisons = Maison.objects.filter(visibilite=True)
    else:
        maisons = Maison.objects.filter(quartier__icontains=search, visibilite=True)
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
    maison = get_object_or_404(Maison, id=id_maison)
    photos = Images.objects.filter(maison=maison)
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
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'appropos.html')

def requette(request):
    if not request.user.is_authenticated:
        return redirect('login')
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
    if not request.user.is_authenticated:
        return redirect('login')
    search = request.GET.get('Search')
    maisons = []
    print(search)
    messages = Message.objects.all()
    users = User.objects.all()
    if search == None:
        maisons = Maison.objects.filter(visibilite=True)
    else:
        maisons = Maison.objects.filter(quartier__icontains=search,visibilite=True)
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
        image = request.FILES.get('image', '')
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
        maison.image = image
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

def error403(request):
    dhb_context = {'messageErr': 'CETTE RESSOURCE REQUIèRE UNE AUTHENTIFICATION !'}
    return render(request, "administrator/error-403.html", dhb_context)

def search(request):
    if request.user.is_authenticated:

        query = request.GET["search"]
        result_object = Maison.objects.filter(name_sch__icontains=query)
        # result_object = result_object.append(School.objects.filter(system_sch__icontains=query))
        rst_srh_context = {'title': 'RESULTATS DE LA RECHERCHE LIEE A : ' + query, 'result_object': result_object}
        return render(request, 'search_resul.html', rst_srh_context)
    else:
        return redirect(error403)

