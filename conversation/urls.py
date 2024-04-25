from django.urls import path
from .views import nova_conversa, inbox, detalhe

app_name = "conversation"

urlpatterns = [
    path('', inbox, name='inbox'),
    path('<int:id>/', detalhe, name='detalhe'),
    path('novo/<int:id>/', nova_conversa, name='novo')
]