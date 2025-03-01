from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    nom = models.CharField(max_length=50)
    prenoms = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    pasword = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom} {self.prenoms}"
    
    class Meta:
        abstract = True

class Client(Utilisateur):
    pass

class Personnel(Utilisateur):
    fonction = models.CharField(max_length=50)
    date_embauche = models.DateField()
    salaire = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images_personnel/', null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenoms} - {self.fonction}"
    

class Administrateur(Personnel):
    # Fonction héritée de la classe Personnel Admin (Absolu)
    fonction = "Administrateur"
    pass