from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Livre

def liste_livres(request):
    livres = Livre.objects.all()
    return render(request, 'bibliotheque/liste_livres.html', {'livres': livres})

def index(request):
    return HttpResponse("<h1>Bienvenue dans l'application Bibliothèque !</h1>")


