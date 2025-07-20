from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from fci.filters import ContatoFilter, ImovelFilter
from fci.models import Bairro, Cidade, Contato, Corretor, Diferencial, FaixaPreco, Galeria, Foto, Imovel, Situacao, Tipo, Uf
from fci.serializers import UploadArquivoSerializer, ContatoReadSerializer, ContatoWriteSerializer, BairroSerializer, CidadeSerializer, CorretorSerializer, DiferencialSerializer, FaixaPrecoSerializer, GaleriaSerializer, FotoSerializer, ImovelSerializer, SituacaoSerializer, TipoSerializer, UfSerializer

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

class UploadArquivoView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = UploadArquivoSerializer(data=request.data)
        if serializer.is_valid():
            arquivo = serializer.validated_data['file']
            
            # Salve o arquivo como desejar, por exemplo:
            # with open('caminho/destino/' + arquivo.name, 'wb+') as destination:
            #     for chunk in arquivo.chunks():
            #         destination.write(chunk)
            return Response({'nome': arquivo.name, 'tamanho': arquivo.size, 'status': status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getUfs(request):
    items = Uf.objects.all()
    serializer = UfSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCidades(request):
    items = Cidade.objects.all()
    serializer = CidadeSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBairros(request):
    items = Bairro.objects.all()
    serializer = BairroSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCorretores(request):
    items = Corretor.objects.all()
    serializer = CorretorSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTipos(request):
    items = Tipo.objects.all()
    serializer = TipoSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getFaixaPrecos(request):
    items = FaixaPreco.objects.all()
    serializer = FaixaPrecoSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSituacoes(request):
    items = Situacao.objects.all()
    serializer = SituacaoSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDiferenciais(request):
    items = Diferencial.objects.all()
    serializer = DiferencialSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getImoveis(request):
    items = Imovel.objects.all()
    serializer = ImovelSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addUf(request):
    serializer = UfSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

class ImovelListView(ListAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['codigo', 'nome', 'tipo', 'situacao']
    filterset_class = ImovelFilter
    renderer_classes = [JSONRenderer]
    ordering_fields = ['nome', 'codigo', 'data_entrega', 'criado_em', 'atualizado_em']
    ordering = ['nome']  # valor padrão

class ContatoViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Contato.objects.all()
    renderer_classes = [JSONRenderer]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ContatoFilter
    ordering_fields = ['nome', 'tipo_imovel__nome', 'criado_em']
    ordering = ['-criado_em']

    def get_serializer_class(self):
        if self.action == 'create':
            return ContatoWriteSerializer
        return ContatoReadSerializer

    def get_filter_backends(self):
        # Evita filtros e ordering no POST
        if self.action == 'list':
            return self.filter_backends
        return []

class GaleriaCreateListView(ListCreateAPIView):
    queryset = Galeria.objects.all()
    serializer_class = GaleriaSerializer

class FotoCreateListView(ListCreateAPIView):
    queryset = Foto.objects.all() 
    serializer_class = FotoSerializer 
