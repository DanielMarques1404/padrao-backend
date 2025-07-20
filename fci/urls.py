from django.urls import path
from . import views

contato_list = views.ContatoViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

urlpatterns = [
    path('ufs', views.getUfs),
    path('corretores', views.getCorretores),
    path('cidades', views.getCidades),
    path('bairros', views.getBairros),
    path('diferenciais', views.getDiferenciais),
    path('tipos', views.getTipos),
    path('faixasPreco', views.getFaixaPrecos),
    path('situacoes', views.getSituacoes),
    path('galerias', views.GaleriaCreateListView.as_view(), name='galeria-create-list'),
    path('fotos', views.FotoCreateListView.as_view(), name='foto-create-list'),
    path('imoveis/', views.ImovelListView.as_view(), name='imovel-list'),
    path('contatos/', contato_list, name='contato-list-create'),

    path('upload-arquivo', views.UploadArquivoView.as_view(), name='upload-arquivo'),

    path('add/', views.addUf),
]