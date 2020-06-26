from .models import Aluno, Avaliacao, Objetivo, CampoExperiencia, Escola, Professor, Turma
from rest_framework import serializers
from rest_framework.serializers import CharField, ValidationError
from django.db.models import Q
from django.contrib.auth.hashers import check_password


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

class ObjetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objetivo
        fields = (
            'id',
            'campo_experiencia',
            'descricao',
            'codigo',
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

class LoginEscolaSerializer(serializers.ModelSerializer):
    user = CharField(required=False, allow_blank=True)
    senha = CharField(required=False, allow_blank=True)
    id = CharField(required=False, allow_blank=False)
    
    class Meta:
        model = Escola
        fields = (
            'user',
            'senha',
            'id'
        )

    def validate(self, data):
        user = data.get("user", None)
        senha = data.get("senha", None)
        id = data.get("id", None)

        validacao = Escola.objects.filter(
            Q(user=user),
            Q(senha=senha),
            Q(id=id)
        ) 

        if validacao.exists() and validacao.count() == 1:
            validacao = validacao.first()
           
        else:
            raise ValidationError("Usuario ou senha incorreto")

        return data
    






