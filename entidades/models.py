from django.db import models

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Escola(Base):
    nome = models.CharField(max_length=300)
    endereco = models.CharField(max_length=500)
    diretor = models.CharField(max_length=300)
    cnpj = models.CharField(max_length=50)
    telefone = models.CharField(max_length=30)
    email = models.EmailField()
    tipo = models.CharField(max_length=2)
    user = models.CharField(max_length=15)
    senha = models.CharField(max_length=16)
    
    class Meta:
        verbose_name = 'Escola'
        verbose_name_plural = 'Escolas'
        ordering = ['id']

    def __str__(self):
        return self.nome

class Professor(Base):
    escola = models.ForeignKey(Escola, related_name='professores', on_delete=models.CASCADE)
    nome = models.CharField(max_length=300)
    cpf = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    email = models.EmailField()
    datanasc = models.DateField()
    user = models.CharField(max_length=15)
    senha = models.CharField(max_length=16)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        ordering = ['id']

    def __str__(self):
        return self.nome

class Turma(Base):
    professor = models.ForeignKey(Professor, related_name='turmas', on_delete=models.CASCADE)
    nome = models.CharField(max_length=500)
    descricao = models.TextField()
    periodo = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['id']

    def __str__(self):
        return self.nome

class Aluno(Base):
    turma = models.ForeignKey(Turma, related_name='alunos', on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, related_name='alunos', on_delete=models.CASCADE)
    nome = models.CharField(max_length=300)
    matricula = models.CharField(max_length=30)
    datanasc = models.DateField()
    sexo = models.CharField(max_length=30)
    nome_responsavel = models.CharField(max_length=300)
    telefone_responsavel = models.CharField(max_length=45)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['id']

    def __str__(self):
        return self.nome

class CampoExperiencia(Base):
    nome = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'campo experiencia'
        verbose_name_plural = 'campos experiencias'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Objetivo(Base):
    campo_experiencia = models.ForeignKey(CampoExperiencia, related_name='objetivos', on_delete=models.CASCADE)
    descricao = models.TextField()
    codigo = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'objetivo'
        verbose_name_plural = 'objetivos'
        ordering = ['descricao']

    def __str__(self):
        return self.codigo

class Avaliacao(Base):
    professor = models.ForeignKey(Professor, related_name='avaliacoes', on_delete=models.PROTECT)
    aluno = models.ForeignKey(Aluno, related_name='avaliacoes', on_delete=models.PROTECT)
    campo_experiencia = models.ForeignKey(CampoExperiencia, related_name='avaliacoes', on_delete=models.PROTECT)
    objetivo = models.ForeignKey(Objetivo, related_name='avaliacoes', on_delete=models.PROTECT)
    avaliacao = models.CharField(max_length=40)
    observacao = models.TextField()

    class Meta:
        verbose_name = 'avaliacao'
        verbose_name_plural = 'avaliacoes'
        ordering = ['id']

    def __str__(self):
        return self.avaliacao

    








