from rest_framework import serializers
from fci.models import User, Bairro, Cidade, Contato, Corretor, Diferencial, FaixaPreco, Galeria, Foto, Imovel, Pretensao, Situacao, Tipo, Uf

class UploadArquivoSerializer(serializers.Serializer):
    file = serializers.FileField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uf
        fields = '__all__'

class CidadeSerializer(serializers.ModelSerializer):
    uf = UfSerializer()
    class Meta:
        model = Cidade
        fields = ['id', 'nome', 'uf']

class BairroSerializer(serializers.ModelSerializer):
    cidade = CidadeSerializer()
    class Meta:
        model = Bairro
        fields = ['id', 'nome', 'cidade']

class CorretorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corretor
        fields = '__all__'
        read_only_fields = ['criado_em', 'atualizado_em']

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'

class FaixaPrecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaixaPreco
        fields = '__all__'     

class SituacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model: Situacao
        fields = '__all__'
        
class DiferencialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diferencial
        fields = '__all__'

class PretensaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pretensao
        fields = '__all__'        

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = '__all__'

class GaleriaSerializer(serializers.ModelSerializer):
    fotos = FotoSerializer(many=True, read_only=True)
    class Meta:
        model = Galeria
        fields = '__all__'

class ImovelSerializer(serializers.ModelSerializer):
    bairro = BairroSerializer()
    tipo = TipoSerializer()
    galerias = GaleriaSerializer(many=True, read_only=True)

    class Meta:
        model = Imovel
        fields = '__all__'    


class ContatoReadSerializer(serializers.ModelSerializer):
    tipo_imovel = TipoSerializer()
    bairro = BairroSerializer()
    class Meta:
        model = Contato
        fields = '__all__'
        read_only_fields = ['criado_em']

class ContatoWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'
        read_only_fields = ['criado_em']