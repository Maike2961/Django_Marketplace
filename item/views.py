from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Item, Category
from .forms import novoItemForm, EditaItemForm

def items(request):
    query = request.GET.get('query', '')
    categoria_id = request.GET.get('categoria', 0)
    categorias = Category.objects.all()
    items = Item.objects.filter(a_venda=False)
    
    if categoria_id:
        items = items.filter(categoria_id=categoria_id)
    
    if query:
        items = items.filter(Q(nome__icontains=query) | Q(descricao__icontains=query))
    context = {
        'items': items,
        'query': query,
        'categorias': categorias,
        'categoria_id': int(categoria_id)
    }
    return render(request, 'item/items.html', context)

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

@login_required
def delete(request, id):
    item = get_object_or_404(Item, id=id, criado_por=request.user)
    item.delete()
    return redirect('dashboard:index')

@login_required
def edita(request, id):
    item = get_object_or_404(Item, id=id, criado_por=request.user)
    if request.method == 'POST':
        form = EditaItemForm(request.POST, request.FILES, instance=item)
        
        if form.is_valid():
            form.save()

            return redirect('item:detalhes', id=item.id)
    else:     
        form = EditaItemForm(instance=item)
        
    context = {
        'form': form,
        'title': 'edita item'
    }
    return render(request, 'item/form.html', context)