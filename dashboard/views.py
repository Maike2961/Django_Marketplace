from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from item.models import Item

@login_required
def index(request):
    items = Item.objects.filter(criado_por=request.user)
    context = {
        'items': items
    }
    return render(request, 'dashboard/dashboard.html', context)
