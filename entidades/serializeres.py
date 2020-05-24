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
            'criacao',
            'senha'
            
        )

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
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
            'criacao'

        )

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = (
            'id',
            'professor',
            'nome',
            'descricao',
            'periodo',
            'criacao'
        )

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
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
            'criacao'
        )

class CampoExperienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampoExperiencia
        fields = (
            'id',
            'nome',
            'criacao'
        )


class ObjetivoSerializer(serializers.ModelSerializer):
    experiencia = CampoExperienciaSerializer(many=True, read_only=True)
    class Meta:
        model = Objetivo
        fields = (
            'id',
            'campo_experiencia',
            'descricao',
            'codigo',
            'criacao',
            'experiencia'
        )

        
class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = (
            'id',
            'professor',
            'aluno',
            'campo_experiencia',
            'objetivo',
            'avaliacao',
            'observacao',
            'criacao'

        )





