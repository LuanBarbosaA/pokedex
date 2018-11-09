from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class Habilidade(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Movimento(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Elemento(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Pokemon(models.Model):
    imagem = models.FileField(upload_to='pokemon/imagens/')
    nome = models.CharField(max_length=200)
    ataque_fisica = models.PositiveIntegerField()
    defesa_fisica = models.PositiveIntegerField()
    ataque_especial = models.PositiveIntegerField()
    defesa_especial = models.PositiveIntegerField()
    vida = models.PositiveIntegerField()
    velocidade = models.PositiveIntegerField()
    experiencia = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    peso = models.PositiveIntegerField()
    habilidades = models.ManyToManyField(Habilidade)
    movimentos = models.ManyToManyField(Movimento)
    elementos = models.ManyToManyField(Elemento)
    evolucao = models.ForeignKey('self', blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
