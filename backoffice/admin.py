from django.contrib import admin
from .models import CategorieMaison
from .models import Maison
from .models import Commande

# Register your models here.
admin.site.register(CategorieMaison)
admin.site.register(Maison)
admin.site.register(Commande)
