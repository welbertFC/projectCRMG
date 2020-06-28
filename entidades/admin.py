from django.contrib import admin
from .models import Aluno, Avaliacao, Objetivo, CampoExperiencia, Escola, Professor, Turma

@admin.register(Escola)
class EscolaAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'nome',
            'endereco',
            'diretor',
            'cnpj',
            'telefone',
            'email',
            'tipo',
            'user',
            'senha'
            
        )
@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        'escola',
        'nome',
        'cpf',
        'telefone',
        'email',
        'datanasc',
        'user',
        'senha'
       
    )

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = (
        'professor',
        'nome',
        'descricao',
        'periodo'
        
    )

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = (
        'turma',
        'professor',
        'nome',
        'matricula',
        'datanasc',
        'sexo',
        'nome_responsavel',
        'telefone_responsavel'
        
    )

@admin.register(CampoExperiencia)
class CampoExperienciaAdmin(admin.ModelAdmin):
    list_display = (
         'nome',
     
    )
    
@admin.register(Objetivo)
class ObjetivoAdmin(admin.ModelAdmin):
    list_display = (
        'campo_experiencia',
        'descricao',
        'codigo'
       
    )

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = (
        'professor',
        'aluno',
        'campo_experiencia',
        'objetivo',
        'avaliacao',
        'observacao'
    )