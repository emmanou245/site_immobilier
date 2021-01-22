from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from backoffice.models import CategorieMaison
from backoffice.models import Commande
from backoffice.models import Maison

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

