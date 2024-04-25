from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from item.models import Item
from .forms import ConversationMessageForm
from .models import Conversation

@login_required
def nova_conversa(request, id):
    item = get_object_or_404(Item, id=id)

    if item.criado_por == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(membros__in=[request.user.id])
    
    if conversations:
        return redirect('conversation:detalhe', id=conversations.first().id)
    
    if request.method == "POST":
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.membros.add(request.user)
            conversation.membros.add(item.criado_por)
            conversation.save()
            
            conversation_message = form.save(commit=False)
            conversation_message.conversa = conversation
            conversation_message.criado_por = request.user
            conversation_message.save()
            
            return redirect('item:detalhes', id=id)
    else:
        form = ConversationMessageForm()
    
    context = {
        'form': form
    }
    return render(request, 'conversations/novo.html', context)

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(membros__in=[request.user.id])
    print(conversations)
    context = {
        'conversations': conversations
    }
    return render(request, 'conversations/inbox.html', context)

@login_required
def detalhe(request, id):
    conversations = Conversation.objects.filter(membros__in=[request.user.id]).get(id=id)
    if request.method == "POST":
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversa = conversations
            conversation_message.criado_por = request.user
            conversation_message.save()
            
            conversations.save()
            
            return redirect('conversation:detalhe', id=id)
    else:
        form = ConversationMessageForm()
    context = {
        'conversations': conversations,
        'form':form
    }
    return render(request, 'conversations/detalhe.html', context)