from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
import uuid

# Create your models here.
class AutomobilioModelis(models.Model):
    marke = models.CharField(_("Markė"), max_length=100, help_text='Iveskite automobilio marke (pvz. ford)' )
    modelis = models.CharField(_("Modelis"), max_length=100)

    class Meta:
        verbose_name = _("Automobilio modelis")
        verbose_name_plural = _("Automobilių modeliai")

    def __str__(self):
        return f"{self.marke} {self.modelis} "

    def get_absolute_url(self):
        return reverse("automobilio_modelis_detail", kwargs={"pk": self.pk})


class Automobilis(models.Model):
    valstybinis_nr = models.CharField(_("valstybinis nr"), max_length=100)
    automobilio_modelis = models.ForeignKey(
        AutomobilioModelis,
        verbose_name=_("Automobilio modelis"),
        on_delete=models.CASCADE,
        related_name='Automobiliai')
    
    photo = models.ImageField(
    _("photo"), 
    upload_to='car_service/vehicle_photos', 
    null=True, 
    blank=True,
    )
    
    # models.CharField(_("automobilio modelis"), max_length=100)
    vin_kodas = models.CharField(_("VIN kodas"), max_length=100)
    klientas = models.CharField(_("Klientas"), max_length=100)

    class Meta:
        verbose_name = _("Automobilis")
        verbose_name_plural = _("Automobiliai")

    def __str__(self):
        return f"{self.valstybinis_nr} {self.vin_kodas} {self.klientas} "

    def get_absolute_url(self):
        return reverse("automobiliss_detail", kwargs={"pk": self.pk})
    
    def display_modelis(self):
        return  ','.join(automobilio_modelis.marke for automobilio_modelis in self.automobilio_modelis.all()[:3])

    
class Uzsakymas(models.Model):
    data = models.IntegerField(_('Data'))
    automobilis = models.ForeignKey(
        Automobilis,
        verbose_name=_("Uzsakymas"),
        on_delete=models.CASCADE,
        related_name='uzsakymai'
    )
    suma = models.IntegerField(_('Suma'))

    class Meta:
        verbose_name = _("Uzsakymas")
        verbose_name_plural = _("Uzsakymai")

    def __str__(self):
        return f"{self.data} {self.automobilis}"

    def get_absolute_url(self):
        return reverse("uzsakymas_detail", kwargs={"pk": self.pk})
    
    def display_automobilis(self):
        return ','.join(automobilis.valstybinis_nr for automobilis in self.automobilis.all()[:3])

class Paslauga (models.Model):
    pavadinimas = models.CharField(_("Pavadinimas"), max_length=100)
    kaina = models.IntegerField(_('Kaina'))

    class Meta:
        verbose_name = _("Paslauga")
        verbose_name_plural = _("Paslaugos")

    def __str__(self):
        return f"{self.pavadinimas} {self.kaina}"

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
    
    def display_paslauga(self):
        return ','.join(paslauga.pavadinimas for paslauga in self.paslauga.all()[:3])
    



class UzsakymoEilute(models.Model):
    paslauga = models.ForeignKey(
        Paslauga,
        verbose_name=_('uzsakumo eilute'),
        on_delete=models.CASCADE,
        related_name='uzsakymu_eilutes'
    )
    uzsakymas = models.ForeignKey(
        Uzsakymas,
        verbose_name=_('uzsakumo eilute'),
        on_delete=models.CASCADE,
        related_name='uzsakymu_eilutes'
    )
    
    kiekis = models.IntegerField(_('Kiekis'))
    kaina = models.IntegerField(_('Kaina'))

    class Meta:
        verbose_name = _("Uzsakymo eilute")
        verbose_name_plural = _("Uzsakymu eilutes")

    def __str__(self):
        return f"{self.paslauga} {self.uzsakymas} {self.kiekis} {self.kaina}"

    def get_absolute_url(self):
        return reverse("uzsakymo_eilute_detail", kwargs={"pk": self.pk})
    
    def display_paslauga(self):
        return ','.join(paslauga.pavadinimas for paslauga in self.paslauga.all()[:3])
