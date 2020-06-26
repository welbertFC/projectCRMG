from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST 
from rest_framework.permissions import AllowAny 
from django.db import models
from .serializers import AlunoSerializer, AvaliacaoSerializer, AlunoSerializer, ObjetivoSerializer, CampoExperienciaSerializer, EscolaSerializer, ProfessorSerializer, TurmaSerializer, LoginEscolaSerializer
from .models import Aluno, Avaliacao, Objetivo, CampoExperiencia, Escola, Professor, Turma
from django.db.models import Q

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

class LoginEscolaViewAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginEscolaSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = LoginEscolaSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data, 
            queryset = Escola.objects.all()
            return Response(queryset, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
   


