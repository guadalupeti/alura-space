from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'publicada', 'data', 'legenda')
    list_display_links = ('id', 'nome','legenda')
    search_fields = ('nome', )
    list_filter = ('categoria', 'data')

admin.site.register(Fotografia, ListandoFotografias)
