from django.shortcuts import render
from item.models import Category, Item

# Create your views here.
def index(request):
    items = Item.objects.filter(a_venda=True)[0:6]
    categorias = Category.objects.all()
    context = {
        'categorias': categorias,
        'items': items
    }
    return render(request, 'core/index.html', context)

def contato(request):
    return render(request, 'core/contato.html')
