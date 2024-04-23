from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import novoItemForm

def detail(request, id):
    print(id)
    item = get_object_or_404(Item, id=id)
    itens_relacionados = Item.objects.filter(categoria=item.categoria, a_venda=False).exclude(id=id)[0:3]
    context = {
        "item":item,
        'itens_relacionados': itens_relacionados
    }
    return render(request, 'item/detalhe.html', context)

@login_required
def novoitem(request):
    if request.method == 'POST':
        form = novoItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.criado_por = request.user
            item.save()

            return redirect('item:detalhes', id=item.id)
    else:     
        form = novoItemForm()
        
    context = {
        'form': form,
        'title': 'novo item'
    }
    return render(request, 'item/form.html', context)