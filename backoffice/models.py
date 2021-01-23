from django.db import models
from django.contrib.auth.models import User
#from django.contrib.gis.db.models import PointField

# Create your models here.
class CategorieMaison(models.Model):
    nom = models.CharField(max_length=256, null=True)

    @staticmethod
    def get_all_categories():
        return CategorieMaison.objects.all()

    def __str__(self):
        return '{}'.format(self.nom)

class Maison(models.Model):
    categorie = models.ForeignKey(CategorieMaison,on_delete=models.DO_NOTHING, default=1, null=True)
    nombre_chambre = models.IntegerField(null=True)
    photo = models.ImageField(upload_to='media/images/', null=True, blank=True)
    description = models.TextField(null=True)
    prix = models.FloatField(null=True)
    quartier = models.CharField(max_length=256,null=True)
    ville = models.CharField(max_length=256, null=True)
    depot_initial = models.CharField(max_length=256,null=True)
    caution = models.FloatField(null=True)
    disponibilite = models.DateTimeField(null=True)
    #location = PointField(null=True,dim=2)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return '{} {} {}'.format(self.categorie,self.ville,self.quartier)

    @staticmethod
    def get_all_maisons():
        return Maison.objects.all()

    @staticmethod
    def get_all_maison_by_categoriesid(categorie_id):
        if categorie_id:
            return Maison.objects.filter(categorie=categorie_id)
        else:
            return Maison.get_all_maisons();

class Commande(models.Model):
    STATUS = (('en instance','en instance'),
            ('non occuper','non occuper'),
            ('occupé','occupé'))
    maison = models.ForeignKey(Maison, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    telephone = models.IntegerField(null=True)
    message = models.TextField(null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.maison,self.user)