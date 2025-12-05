from django.db import models
from django.utils import timezone # Importante para pegar o ano atual


class Usuario(models.Model):
    class Tipo(models.TextChoices):
        ALUNO = 'ALUNO', 'Aluno'
        PROFESSOR = 'PROFESSOR', 'Professor'
        ADMIN = 'ADMIN', 'Administrador'

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
   
    criado_em = models.DateTimeField(auto_now_add=True)
    
    tipo_usuario = models.CharField(
        max_length=20, 
        choices=Tipo.choices, 
        default=Tipo.ALUNO
    )

    class Meta:
        ordering = ['nome']

    def _str(self): # Corrigido de str para __str_
        return self.nome

