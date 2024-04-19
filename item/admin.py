from django.contrib import admin

from .models import Category, Item

admin.site.register(Category)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'categoria', 'preco', 'criado_por', 'criado_em', 'a_venda')
