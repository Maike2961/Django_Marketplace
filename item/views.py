from django.shortcuts import render, get_object_or_404
from .models import Item

def detail(request, id):
    item = get_object_or_404(Item, id=id)
    context = {
        "item":item
    }
    return render(request, 'item/detalhe.html', context)