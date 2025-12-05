from django.contrib import admin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'senha', 'tipo_usuario', 'criado_em',)
    search_fields = ('nome', 'email')
    ordering = ('nome',)