from django.contrib import admin
from .models import CategorieMaison
from .models import Ville
from .models import Quartier
from .models import Maison
from .models import Commande
from .models import Requette
from .models import Message
from .models import Images
from .models import Commentaire



# Register your models here.
admin.site.register(CategorieMaison)
admin.site.register(Ville)
admin.site.register(Quartier)
admin.site.register(Commande)
admin.site.register(Requette)
admin.site.register(Message)
admin.site.register(Commentaire)


class ImagesAdmin(admin.StackedInline):
    model = Images

@admin.register(Maison)
class MaisonAdmin(admin.ModelAdmin):
    inlines = [ImagesAdmin]

    class Meta:
       model = Maison

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass

