from django.db import models
# Create your models here.
class Usuario(models.Model):
    class Tipo(models.TextChoices):
        ALUNO = 'ALUNO', 'Aluno'
        PROFESSOR = 'PROFESSOR', 'Professor'


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

    def _str_(self):
        return self.nome