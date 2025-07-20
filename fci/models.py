from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

class Uf(models.Model):
    sigla = models.CharField(max_length=2, unique=True)
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nome} ({self.sigla})"

class Cidade(models.Model):
    uf = models.ForeignKey(Uf, on_delete=models.PROTECT, related_name="cidades")
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} ({self.uf.sigla})"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['uf', 'nome'], name='cidade_unica_por_uf')
        ]

class Bairro(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, related_name="bairros")
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} ({self.cidade.nome})"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cidade', 'nome'], name='bairro_unico_por_cidade')
        ]

# Pessoas

class User(AbstractUser):
    telefone = models.CharField(max_length=25, blank=True, null=True)

class Corretor(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    creci = models.CharField(max_length=150, unique=True)
    descricao = models.CharField(max_length=2000)
    imagem = models.CharField(max_length=150)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    url = models.CharField(max_length=1000)

# IMÓVEIS

class Tipo(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class FaixaPreco(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    valor_inicial = models.DecimalField(max_digits=15, decimal_places=2)
    valor_final = models.DecimalField(max_digits=15, decimal_places=2)
    ativo = models.BooleanField(default=True)

class Situacao(models.Model):
    nome = models.CharField(max_length=150, unique=True)    
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Diferencial(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    icone = models.CharField(max_length=255, blank=True, null=True)
    ativo = models.BooleanField(default=True)

class Pretensao(models.Model):
    nome = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nome

formato_validator_numeros_variaveis = RegexValidator(
    regex=r'^\d{2}(-\d{2})?$',
    message='O valor deve estar no formato "99" ou "99-99".'
)

class Galeria(models.Model):
    imovel = models.ForeignKey('Imovel', on_delete=models.CASCADE, related_name='galerias')
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.imovel.nome} - {self.nome}"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['imovel', 'nome'], name='unique_nome_galeria_por_imovel')
        ]

    
class Foto(models.Model):
    galeria = models.ForeignKey(Galeria, on_delete=models.CASCADE, related_name="fotos")
    file_path = models.CharField(max_length=500)
    file_name = models.CharField(max_length=255)
    destaque = models.BooleanField(default=False)
    nome = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.file_path}/{self.file_name} ({self.galeria.dominio.nome})"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['galeria', 'file_path', 'file_name'], name='foto_unica_por_galeria')
        ]


class Imovel(models.Model):
    codigo = models.CharField(max_length=15, unique=True)
    nome = models.CharField(max_length=255, unique=True)
    pretensao = models.ForeignKey(Pretensao, on_delete=models.PROTECT, related_name="imoveis")
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, related_name="imoveis")
    situacao = models.ForeignKey(Situacao, on_delete=models.PROTECT, related_name="imoveis")
    cep = models.CharField(max_length=25)
    logradouro = models.CharField(max_length=255)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=10)
    bairro = models.ForeignKey(Bairro, on_delete=models.PROTECT, related_name="imoveis")
    ponto_referencia = models.CharField(max_length=2000)
    quartos = models.CharField(
        max_length=5,
        validators=[formato_validator_numeros_variaveis],
        help_text='Formato permitido: 99 ou 99-99'
    )
    suites = models.CharField(
        max_length=5,
        validators=[formato_validator_numeros_variaveis],
        help_text='Formato permitido: 99 ou 99-99'
    )
    banheiros = models.CharField(
        max_length=5,
        validators=[formato_validator_numeros_variaveis],
        help_text='Formato permitido: 99 ou 99-99'
    )
    vagas = models.CharField(
        max_length=5,
        validators=[formato_validator_numeros_variaveis],
        help_text='Formato permitido: 99 ou 99-99'
    )
    area_inicial = models.DecimalField(max_digits=15, decimal_places=2)
    area_final = models.DecimalField(max_digits=15, decimal_places=2)
    data_entrega = models.DateTimeField(null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.codigo} - {self.nome}"


class Contato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    telefone = models.CharField(max_length=25)
    tipo_imovel = models.ForeignKey(Tipo, on_delete=models.PROTECT, related_name="contatos")
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    bairro = models.ForeignKey(Bairro, on_delete=models.PROTECT, related_name="contatos")
    criado_em = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(max_length=2000, blank=True, null=True)
    status = models.BooleanField(default=False)