from django.contrib import admin
from .models import Usuario, Materia, Assunto
# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'tipo_usuario', 'criado_em')
    search_fields = ('nome', 'email')
    ordering = ('nome',)

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
    ordering = ('nome',)

@admin.register(Assunto)
class AssuntoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'usuario_criador_id', 'materia_id')
    search_fields = ('titulo', 'descricao',)
    ordering = ('titulo',)
