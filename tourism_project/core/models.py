from django.db import models
from django.contrib.auth.models import AbstractUser

class Sede(models.Model):
    nome = models.CharField(max_length=255)
    indirizzo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class TipoUtente(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class CustomUser(AbstractUser):
    tipo_utente = models.ForeignKey(TipoUtente, on_delete=models.CASCADE, related_name='utenti')
    nome = models.CharField(max_length=150)
    cognome = models.CharField(max_length=150)
    data_nascita = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    sede = models.CharField(max_length=255, null=True, blank=True)
    responsabile = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username}"
