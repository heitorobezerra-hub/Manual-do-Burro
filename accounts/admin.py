from django.contrib import admin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'tipo_usuario', 'criado_em', 'matricula', 'senha')
    search_fields = ('matricula', 'email')
    ordering = ('matricula',)