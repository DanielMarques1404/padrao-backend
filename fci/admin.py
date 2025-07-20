from django.contrib import admin

from fci.models import Uf, Cidade, Bairro, User, Diferencial, Pretensao, Situacao, Imovel, Contato

class UfAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('sigla', 'nome',)
    search_fields = ('sigla', 'nome',)
    # list_display_links = ('id', 'sigla')
    # search_fields = ('sigla',)
    # list_filter = ('categoria',)
    # list_editable = ('publicada', )
    # list_per_page = 5

class CidadeAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('nome','uf',)
    search_fields = ('nome', 'uf__sigla',)

class BairroAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('nome', 'cidade',)
    search_fields = ('nome', 'cidade__nome',)

class UserAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('username', 'first_name', 'last_name', 'email', 'telefone',)
    search_fields = ('username', 'first_name', 'last_name', 'email',)

class DiferencialAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('nome', 'ativo',)
    ordering = ('nome',)

class ImovelAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('nome', 'tipo', 'situacao')

class PretensaoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('nome', )
    ordering = ('nome',)

class SituacaoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('nome', )
    ordering = ('nome',)

class ContatoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('nome', 'email', 'telefone', 'status', 'criado_em')
    
admin.site.register(Uf, UfAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Bairro, BairroAdmin)

admin.site.register(User, UserAdmin)

admin.site.register(Diferencial, DiferencialAdmin)
admin.site.register(Pretensao, PretensaoAdmin)
admin.site.register(Situacao, SituacaoAdmin)    
admin.site.register(Imovel, ImovelAdmin)

admin.site.register(Contato, ContatoAdmin)
