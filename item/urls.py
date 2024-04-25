from django.urls import path

from .views import detail, novoitem, delete, edita, items

app_name = 'item'

urlpatterns = [
    path('<int:id>/', detail, name='detalhes'),
    path('delete/<int:id>',delete, name='delete'),
    path('edita/<int:id>', edita, name='edita'),
    path('novo_item/', novoitem, name='novo_item'),
    path('', items, name='items')
]