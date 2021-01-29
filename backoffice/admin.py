from django.contrib import admin
from .models import CategorieMaison
from .models import Maison
from .models import Commande
from .models import Requette
from .models import Message
from .models import Images

# Register your models here.
admin.site.register(CategorieMaison)
admin.site.register(Commande)
admin.site.register(Requette)
admin.site.register(Message)


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

