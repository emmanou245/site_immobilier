from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from backoffice.models import CategorieMaison
from backoffice.models import Commande
from backoffice.models import Maison
from backoffice.models import Requette
from backoffice.models import Commentaire
from backoffice.models import Message
from backoffice.models import Images
from backoffice.models import Ville
from backoffice.models import Quartier
from .forms import LoginForm,SignupForm
from django.db.models import Q
#import folium

# Create your views here.
def home(request):
    if not request.user.is_authenticated :
        return redirect('login')
    commandes = Commande.objects.all()
    users = User.objects.all()
    liste_categories = CategorieMaison.objects.all()
    liste_villes = Ville.objects.all()
    maisons = Maison.objects.all()
    liste_quartiers = Quartier.objects.all()
    commentaires = Commentaire.objects.filter(visibilite=True)
    if request.method == 'POST':
        categorie_id = request.POST.get('categorie_id','')
        ville_id = request.POST.get('ville_id','')
        quartier_id = request.POST.get('quartier_id','')
        maisons = Maison.objects.filter(Q(categorie=CategorieMaison.objects.get(id=categorie_id) | Q(ville=Ville.objects.get(id=ville_id) | Q(quartier=Quartier.objects.get(id=quartier_id)))))
        print(categorie_id, ville_id, quartier_id)
    return render(request,'index.html',locals())


def inscrire(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            row_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=row_password)
            return redirect('login')
    return render(request, "signup.html", {'form': form})

def connecter(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    commentaires = Commentaire.objects.filter(visibilite=True)
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
        return redirect('/')
    context = {'form': form, 'commentaires':commentaires}
    return render(request, "login.html",context)

def deconnecter(request):
    logout(request)
    return redirect('login')

def detail_maison(request,id_maison):
    maison = get_object_or_404(Maison, id=id_maison)
    photos = Images.objects.filter(maison=maison)
    commentaires = Commentaire.objects.filter(visibilite=True)
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

def requette(request):
    if not request.user.is_authenticated:
        return redirect('login')
    liste_categories = CategorieMaison.objects.all()
    liste_villes = Ville.objects.all()
    liste_quartiers = Quartier.objects.all()
    if request.method == 'POST':
        categorie_id = request.POST.get('categorie_id', '')
        ville_id = request.POST.get('ville_id', '')
        quartier_id = request.POST.get('quartier_id', '')
        nombre_chambre = request.POST.get('nombre_chambre', '')
        message = request.POST.get('message', '')
        telephone = request.POST.get('telephone', '')
        prix = request.POST.get('prix', '')
        requette = Requette()
        categorie = CategorieMaison.objects.get(id=categorie_id)
        ville = Ville.objects.get(id=ville_id)
        quartier = Quartier.objects.get(id=quartier_id)
        requette.categorie = categorie
        requette.ville = ville
        requette.quartier = quartier
        requette.nombre_chambre = nombre_chambre
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
        maisons = Maison.objects.filter(quartier__nom__icontains=search, visibilite=True)
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
    if not request.user.is_authenticated:
        return redirect('login')
    liste_categories = CategorieMaison.objects.all()
    liste_villes = Ville.objects.all()
    liste_quartiers = Quartier.objects.all()
    if request.method == 'POST':
        categorie_id = request.POST.get('categorie_id', '')
        ville_id = request.POST.get('ville_id', '')
        quartier_id = request.POST.get('quartier_id', '')
        nombre_chambre = request.POST.get('nombre_chambre', '')
        image = request.FILES.get('image', '')
        description = request.POST.get('description', '')
        prix = request.POST.get('prix', '')
        depot_initial = request.POST.get('depot_initial','')
        caution = request.POST.get('caution','')
        disponibilite = request.POST.get('disponibilite', '')
        maison = Maison()
        categorie = CategorieMaison.objects.get(id=categorie_id)
        ville = Ville.objects.get(id=ville_id)
        quartier = Quartier.objects.get(id=quartier_id)
        maison.categorie = categorie
        maison.ville = ville
        maison.quartier = quartier
        maison.nombre_chambre = nombre_chambre
        maison.image = image
        maison.description = description
        maison.prix = prix
        maison.depot_initial = depot_initial
        maison.caution = caution
        maison.disponibilite = disponibilite
        maison.user = request.user
        maison.save()
        return redirect('anonce')
    return render(request, 'ajouter_maison.html',locals())

def commentaire_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    commentaires = Commentaire.objects.all()
    if request.method == 'POST':
        photo = request.FILES.get('photo', '')
        nom = request.POST.get('nom', '')
        prenom = request.POST.get('prenom', '')
        commentaire = request.POST.get('commentaire', '')
        commenter = Commentaire()
        commenter.photo = photo
        commenter.nom = nom
        commenter.prenom = prenom
        commenter.commentaire = commentaire
        commenter.user = request.user
        commenter.save()
        return redirect('/')
    return render(request, 'commentair.html',{'liste_commentaire' : commentaires})

def suggetion_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    commentaires = Commentaire.objects.all()
    if request.method == 'POST':
        photo = request.FILES.get('photo', '')
        commentaire = request.POST.get('commentaire', '')
        commenter = Commentaire()
        commenter.photo = photo
        commenter.commentaire = commentaire
        commenter.user = request.user
        commenter.save()
        return redirect('login')
    return render(request, 'suggetion.html',{'liste_commentaire' : commentaires})

def sug_view(request):

    return render(request, 'sug.html')

