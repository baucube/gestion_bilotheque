from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Livre

class LivreTestCase(TestCase):
    def setUp(self):
        Livre.objects.create(name="Livre 1", auteur="Auteur 1")

    def test_livre_creation(self):
        livre = Livre.objects.get(name="Livre 1")
        self.assertEqual(livre.auteur, "Auteur 1")

