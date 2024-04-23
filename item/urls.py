from django.urls import path

from .views import detail, novoitem

app_name = 'item'

urlpatterns = [
    path('<int:id>/', detail, name='detalhes'),
    path('novo_item/', novoitem, name='novo_item')
]