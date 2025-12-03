from django.db import models
from accounts.models import Usuario
# Create your models here.

    
class Materia(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Assunto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    usuario_criador_id = models.ForeignKey(Usuario, on_delete=models.CASCADE,)
    materia_id = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='assunto')

    class Meta:
        ordering = ['materia_id', 'titulo']

    def __str__(self):
        return self.titulo