import uuid

from django.db import models

# Create your models here.

class LegalBasisChoices(models.TextChoices):
    PRAZO_POS_MORTE_AUTOR = 'PRAZO_POS_MORTE_AUTOR', 'Prazo pós morte do autor'
    PRAZO_DESDE_DIVULGACAO = 'PRAZO_DESDE_DIVULGACAO', 'Prazo após o lançamento de um filme'
    AUTOR_DESCONHECIDO = 'AUTOR_DESCONHECIDO', 'Autor desconhecido, portanto não pode reivindicar os direitos autorais'
    RENUNCIA_DIREITOS = 'RENUNCIA_DIREITOS', 'Autor renunciou aos direitos autorais da obra'
    OUTRO = 'OUTRO', 'Outro motivo que não se enquadra nos anteriores'


class Work(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255, blank=True)
    synopsis = models.TextField()
    language = models.CharField(max_length=255)
    release_date = models.SmallIntegerField(null=True, blank=True)
    image_url = models.URLField()
    magnetic_link = models.CharField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)
    legal_basis = models.CharField(max_length=255, choices=LegalBasisChoices.choices)
    observation_check = models.TextField(blank=True)

    class Meta: 
        abstract = True


class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name