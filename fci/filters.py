import django_filters
from .models import Contato, Imovel

class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass

class ImovelFilter(django_filters.FilterSet):
    situacao = NumberInFilter(field_name='situacao', lookup_expr='in')
    tipo = NumberInFilter(field_name='tipo', lookup_expr='in')
    nome = django_filters.CharFilter(field_name='nome', lookup_expr='icontains')
    codigo = django_filters.CharFilter(field_name='codigo', lookup_expr='icontains')
    
    class Meta:
        model = Imovel
        fields = ['codigo', 'nome', 'tipo', 'situacao']


class ContatoFilter(django_filters.FilterSet):
    criado_em_de = django_filters.DateTimeFilter(field_name='criado_em', lookup_expr='gte')
    criado_em_ate = django_filters.DateTimeFilter(field_name='criado_em', lookup_expr='lte')
    status = django_filters.BooleanFilter(field_name='status')

    class Meta:
        model = Contato
        fields = ['criado_em_de', 'criado_em_ate', 'status']

