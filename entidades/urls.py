from django.urls import path
from django.contrib import admin
from rest_framework.routers import SimpleRouter
from entidades.views import EscolaViewSet, ProfessorViewSet, TurmaViewSet, AlunoViewSet, CampoExperienciaViewSet, ObjetivoViewSet, AvaliacaoViewSet
from .views import LoginEscolaViewAPIView

router = SimpleRouter()
router.register('escola', EscolaViewSet)
router.register('professor', ProfessorViewSet)
router.register('turma', TurmaViewSet)
router.register('aluno', AlunoViewSet)
router.register('campo_experiencia', CampoExperienciaViewSet)
router.register('objetivo', ObjetivoViewSet)
router.register('avaliacao', AvaliacaoViewSet)


urlpatterns = [
    path('loginescola/', LoginEscolaViewAPIView.as_view(), name='loginescola'),
 ]
