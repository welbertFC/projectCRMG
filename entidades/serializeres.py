from .models import Aluno, Avaliacao, Objetivo, CampoExperiencia, Escola, Professor, Turma
from rest_framework import serializers


class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = (
            'id',
            'nome',
            'endereco',
            'diretor',
            'cnpj',
            'telefone',
            'email',
            'tipo',
            'user',
            'senha',
            'datatime_create'
        )

class ProfessorSerializer(serializers.ModelSerializer):
    model = Professor
    fields = (
        'id',
        'escola',
        'nome',
        'cpf',
        'telefone',
        'email',
        'datanasc',
        'user',
        'senha',
        'datatime_create'

    )

class TurmaSerializer(serializers.ModelSerializer):
    model = Turma
    fields = (
        'id',
        'professor',
        'nome',
        'descricao',
        'periodo',
        'datatime_create'
    )

class AlunoSerializer(serializers.ModelSerializer):
    model = Aluno
    fields = (
        'id',
        'turma',
        'professor',
        'nome',
        'matricula',
        'datanasc',
        'sexo',
        'nome_responsavel',
        'telefone_responsavel',
        'datatime_create'
    )

class CampoExperienciaSerializer(serializers.ModelSerializer):
    model = CampoExperiencia
    fields = (
        'id',
        'nome',
        'datatime_create'
    )

class ObjetivoSerializer(serializers.ModelSerializer):
    model = Objetivo
    fields = (
        'id',
        'campo_experiencia',
        'descricao',
        'codigo',
        'datatime_create'
    )
class AvaliacaoSerializer(serializers.ModelSerializer):
    model = Avaliacao
    fields = (
        'id',
        'professor',
        'aluno',
        'objetivo',
        'avaliacao',
        'observacao',
        'datatime_create'

    )





