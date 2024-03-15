from django.db import models
from datetime import datetime

class Fotografia(models.Model):

    opcoes_categoria = [
        ('nebulosa', 'Nebulosa'),
        ('estrela', 'Estrela'),
        ('galáxia', 'Galáxia'),
        ('planeta', 'Planeta')
    ]

    opcoes_publicacao = [
        (True, "Publicado"),
        (False, "Não Publicado"),
    ]

    nome = models.CharField(max_length = 100, null = False, blank = False)
    legenda = models.CharField(max_length = 100, null = False, blank = False)
    categoria = models.CharField(max_length = 100, null = False, choices = opcoes_categoria, default = '', blank = False)
    desc = models.TextField(null = False, blank = False)
    foto = models.ImageField(upload_to="fotos", blank = '')
    publicada = models.BooleanField(choices = opcoes_publicacao, default = False)
    data = models.DateTimeField(default = datetime.now, blank = False)

    def __str__(self):
        return f'Nome: {self.nome}'
