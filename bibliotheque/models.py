from django.db import models

# Classe parente pour les médias
class Media(models.Model):
    name = models.CharField(max_length=255)
    date_emprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey('Membre', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True

# Sous-classes héritant de Media
class Livre(Media):
    auteur = models.CharField(max_length=255)

class DVD(Media):
    realisateur = models.CharField(max_length=255)

class CD(Media):
    artiste = models.CharField(max_length=255)

# Classe pour les jeux de plateau
class JeuDePlateau(models.Model):
    name = models.CharField(max_length=255)
    createur = models.CharField(max_length=255)

# Classe pour les membres
class Membre(models.Model):
    name = models.CharField(max_length=255)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Classe pour gérer les emprunts
class Emprunt(models.Model):
    livre = models.ForeignKey('Livre', null=True, blank=True, on_delete=models.CASCADE)
    dvd = models.ForeignKey('DVD', null=True, blank=True, on_delete=models.CASCADE)
    cd = models.ForeignKey('CD', null=True, blank=True, on_delete=models.CASCADE)
    membre = models.ForeignKey('Membre', on_delete=models.CASCADE)
    date_emprunt = models.DateField(auto_now_add=True)
    date_retour = models.DateField()

    def save(self, *args, **kwargs):
        # Vérification des règles métiers avant d'enregistrer
        media = self.livre or self.dvd or self.cd
        if media and not media.disponible:
            raise ValueError("Ce média n'est pas disponible pour l'emprunt.")

        if Emprunt.objects.filter(membre=self.membre, date_retour__gte=self.date_emprunt).count() >= 3:
            raise ValueError("Le membre a déjà 3 emprunts actifs.")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.membre.name} - {self.livre or self.dvd or self.cd}"
