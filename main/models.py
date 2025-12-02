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