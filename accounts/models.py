from django.db import models
from django.utils import timezone # Importante para pegar o ano atual

class Usuario(models.Model):
    class Tipo(models.TextChoices):
        ALUNO = 'ALUNO', 'Aluno'
        PROFESSOR = 'PROFESSOR', 'Professor'
        ADMIN = 'ADMIN', 'Administrador'

    email = models.EmailField(unique=True)
    
    # Campo matrícula agora pode ficar em branco no formulário (blank=True)
    # e não é editável (editable=False)
    matricula = models.CharField(max_length=10, unique=True, blank=True, editable=False)
    senha = models.CharField(max_length=50, null=False)
    
    criado_em = models.DateTimeField(auto_now_add=True)
    
    tipo_usuario = models.CharField(
        max_length=20, 
        choices=Tipo.choices, 
        default=Tipo.ALUNO
    )

    class Meta:
        ordering = ['matricula']

    def _str(self): # Corrigido de str para __str_
        return self.matricula

    def save(self, *args, **kwargs):
        # Se a matrícula ainda não existe (é um cadastro novo)
        if not self.matricula:
            # 1. Pega o ano atual (Ex: 2025)
            agora = timezone.now()
            ano_atual = agora.year
            ano_dois_digitos = str(ano_atual)[-2:] # "25"

            # 2. Conta quantos usuários foram criados neste ano
            qtd_ano = Usuario.objects.filter(criado_em__year=ano_atual).count()
            
            # 3. Gera a sequência (Ex: 5 usuários existem, este é o 6)
            sequencia = qtd_ano + 1

            # 4. Formata: "25" + "0006" = "250006"
            self.matricula = f"{ano_dois_digitos}{sequencia:04d}"

        super().save(*args, **kwargs)