from django.db import models
from utilisateur.models import *
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import os

# Définition des choix
STATUS = (
    ("Non", "Non"),
    ("Oui", "Oui")
)

TYPE_CHOICES = {
    "Simple": "Chambre Simple",
    "Double": "Chambre Double",
    "Suite": "Suite",
    "Familiale": "Chambre Familiale",
    "Executive": "Chambre Executive",
    "Deluxe": "Chambre Deluxe",
    "Junior Suite": "Junior Suite",
    "Presidentielle": "Suite Présidentielle",
    "Chambre avec vue mer": "Chambre avec vue mer",
    "Chambre avec vue jardin": "Chambre avec vue jardin",
    "Chambre communicante": "Chambre communicante",
    "Chambre accessible aux PMR": "Chambre accessible aux personnes à mobilité réduite"
}

# Modèle Hotel
class Hotel(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()
    image = models.ImageField(upload_to='images_hotel/', null=True, blank=True)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

# Modèle Etage
class Etage(models.Model):
    numero_etage = models.PositiveIntegerField()

# Modèle ChambreHotel
class ChambreHotel(models.Model):
    numeroChambre = models.PositiveIntegerField(unique=True)
    type = models.CharField(choices=TYPE_CHOICES.items(), default="Simple", max_length=50)
    etage = models.PositiveIntegerField()
    prix = models.PositiveIntegerField()
    petit_dejeuner = models.CharField(choices=STATUS, default="Non")
    disponibilite = models.CharField(choices=STATUS, default="Oui")
    description = models.TextField()
    image = models.ImageField(upload_to='images_chambre/', null=True, blank=True)

    def __str__(self):
        return f"Chambre N° {self.numeroChambre} - Etage : {self.etage}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

@receiver(pre_delete, sender=ChambreHotel)
def delete_post_image(sender, instance, **kwargs):
    if instance.image and os.path.isfile(instance.image.path):
        os.remove(instance.image.path)

# Modèle Reservation
class Reservation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    chambre = models.ForeignKey(ChambreHotel, on_delete=models.CASCADE)
    nombre_personnes = models.PositiveIntegerField()
    nombre_nuits = models.PositiveIntegerField()
    petit_dejeuner = models.CharField(choices=STATUS, default="Non")
    montant = models.PositiveIntegerField(editable=False)
    date_reservation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Réservation de {self.client} - Chambre {self.chambre.numeroChambre} - {self.date_reservation}"

    def save(self, *args, **kwargs):
        self.montant = self.chambre.prix * self.nombre_nuits
        if self.petit_dejeuner == "Oui":
            self.montant += 5000
        if self.nombre_personnes > 1:
            self.montant += 5000 * (self.nombre_personnes - 1)
        if self.chambre.disponibilite == "Oui":
            self.chambre.disponibilite = "Non"
            self.chambre.save()
        super().save(*args, **kwargs)
