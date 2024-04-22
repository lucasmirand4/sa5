from django.db import models

# Create your models here.
class Pessoa(models.Model):
    """ class Pessoa
    -
    Fields:
    - 'nome' = String
    - 'email' = String
    - 'idade' = Int
    """
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
