from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import CadastroForm

# Create your views here.
def index(request):
    print(request.user)
    items = Item.objects.filter(a_venda=True)[0:6]
    categorias = Category.objects.all()
    context = {
        'categorias': categorias,
        'items': items
    }
    return render(request, 'core/index.html', context)

def contato(request):
    return render(request, 'core/contato.html')

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
       form = CadastroForm()
    context = {
        'form': form
        }
        
    
    return render(request, 'core/cadastro.html', context)