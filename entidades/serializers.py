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
    id_escola = serializers.SerializerMethodField()
    
    class Meta:
        model = Escola
        fields = (
            'id',
            'user',
            'id_escola',
            'senha'
        )

    def validate(self, data):
        user = data.get("user", None)
        senha = data.get("senha", None)
        
        

        if not senha:
            raise ValidationError("senha não encontrado")

        validacao = Escola.objects.filter(
            Q(user=user)
        ) 

        if validacao.exists() and validacao.count() == 1:
            validacao = validacao.first()
        else:
            raise ValidationError("Usuario ou senha incorreto")

        return data
    
    def get_id_escola(self, data):
        id_escola = data.get("id",None)

        id_escola = Escola.objects.filter(
            Q(id=id_escola)
        )

        return id_escola






