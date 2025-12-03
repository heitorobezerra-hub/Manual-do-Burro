from django.contrib import admin
from .models import Materia, Assunto



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
