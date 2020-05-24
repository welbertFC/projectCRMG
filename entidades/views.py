from django.shortcuts import render
from rest_framework import viewsets
from django.db import models
from .serializers import AlunoSerializer, AvaliacaoSerializer, AlunoSerializer, ObjetivoSerializer, CampoExperienciaSerializer, EscolaSerializer, ProfessorSerializer, TurmaSerializer
from .models import Aluno, Avaliacao, Objetivo, CampoExperiencia, Escola, Professor, Turma


class EscolaViewSet(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CampoExperienciaViewSet(viewsets.ModelViewSet):
    queryset = CampoExperiencia.objects.all()
    serializer_class = CampoExperienciaSerializer

class ObjetivoViewSet(viewsets.ModelViewSet):
    queryset = Objetivo.objects.all()
    serializer_class = ObjetivoSerializer

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

