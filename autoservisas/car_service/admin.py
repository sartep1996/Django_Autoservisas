from django.contrib import admin
from . import models

# Register your models here.

from .models import AutomobilioModelis, Automobilis, Uzsakymas, Paslauga, UzsakymoEilute

class AutomobilioAdmin(admin.ModelAdmin):
    list_display = ('valstybinis_nr', 'automobilio_modelis', 'vin_kodas', 'klientas')
    list_filter = ('automobilio_modelis', )
    search_fields = ('valstybinis_nr', 'vin_kodas')

class AutomobilioModelisAdmin(admin.ModelAdmin):
    list_display = ('marke', 'modelis')

class UzsakymoEiluteInLine(admin.TabularInline):
    model = models.UzsakymoEilute
    extra = 0


class UzsaymoEiluteAdmin(admin.ModelAdmin):
    list_display = ('paslauga', 'uzsakymas', 'kiekis', 'kaina')


class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ('data', 'automobilis', 'suma')
    inlines = [UzsakymoEiluteInLine]
 

class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'kaina')


admin.site.register(AutomobilioModelis, AutomobilioModelisAdmin)
admin.site.register(Automobilis, AutomobilioAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(Paslauga, PaslaugaAdmin)
admin.site.register(UzsakymoEilute, UzsaymoEiluteAdmin)

