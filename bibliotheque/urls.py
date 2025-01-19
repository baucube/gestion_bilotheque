from django.urls import path
from . import views

urlpatterns = [
    # Exemple : une vue de base pour tester
    path('', views.index, name='index'),
]
