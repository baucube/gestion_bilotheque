from django.contrib import admin
from .models import Livre, DVD, CD, JeuDePlateau, Membre, Emprunt

@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ('name', 'auteur', 'disponible', 'date_emprunt')
    list_editable = ('disponible',)
    search_fields = ('name', 'auteur')

@admin.register(DVD)
class DVDAdmin(admin.ModelAdmin):
    list_display = ('name', 'realisateur', 'disponible', 'date_emprunt')
    search_fields = ('name', 'realisateur')

@admin.register(CD)
class CDAdmin(admin.ModelAdmin):
    list_display = ('name', 'artiste', 'disponible', 'date_emprunt')
    search_fields = ('name', 'artiste')

@admin.register(JeuDePlateau)
class JeuDePlateauAdmin(admin.ModelAdmin):
    list_display = ('name', 'createur')
    search_fields = ('name',)

@admin.register(Membre)
class MembreAdmin(admin.ModelAdmin):
    list_display = ('name', 'bloque')
    search_fields = ('name',)

@admin.register(Emprunt)
class EmpruntAdmin(admin.ModelAdmin):
    list_display = ('media', 'membre', 'date_emprunt', 'date_retour')
    list_filter = ('date_emprunt', 'date_retour')
