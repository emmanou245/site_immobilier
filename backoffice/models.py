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
    user = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    categorie = models.ForeignKey(CategorieMaison,on_delete=models.DO_NOTHING, default=1, null=True)
    visibilite = models.BooleanField(default=False)
    nombre_chambre = models.IntegerField(null=True)
    image = models.FileField(blank=True,null=True)
    description = models.TextField(null=True)
    prix = models.FloatField(null=True)
    quartier = models.CharField(max_length=256,null=True)
    ville = models.CharField(max_length=256, null=True)
    depot_initial = models.CharField(max_length=256,null=True,blank=True)
    caution = models.FloatField(null=True,blank=True)
    disponibilite = models.DateTimeField(null=True)
    #location = PointField(null=True,dim=2)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return '{} de {} {} {}'.format(self.categorie,self.user,self.ville,self.quartier,self.prix)

class Images(models.Model):
    maison = models.ForeignKey(Maison, null=True, on_delete=models.CASCADE,default=None)
    images = models.FileField(upload_to='images/',null=True)
    def __str__(self):
        return "{} {}".format(self.maison.categorie,self.maison.ville)


class Commande(models.Model):
    STATUS = (('en instance','en instance'),
            ('non occuper','non occuper'),
            ('occupé','occupé'))
    maison = models.ForeignKey(Maison, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=256, null=True, choices=STATUS)
    telephone = models.IntegerField(null=True)
    message = models.TextField(null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.maison,self.user)


class Requette(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    categorie = models.ForeignKey(CategorieMaison,on_delete=models.DO_NOTHING, default=1, null=True)
    nombre_chambre = models.IntegerField(null=True)
    ville = models.CharField(max_length=256, null=True)
    quartier = models.CharField(max_length=256, null=True)
    message = models.TextField(null=True)
    telephone = models.IntegerField(null=True)
    prix = models.FloatField(null=True)

    def __str__(self):
        return '{} {}'.format(self.user, self.categorie)

class Message(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    message = models.TextField(null=True)
    telephone = models.IntegerField(null=True)
    def __str__(self):
        return '{} {}'.format(self.user, self.telephone)


