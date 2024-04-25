from django.db import models
from item.models import Item
from django.contrib.auth.models import User

class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    membros = models.ManyToManyField(User, related_name='conversations')
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('modificado_em',)
    
    
class ConversationMessage(models.Model):
    conversa = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey(User, related_name='message_criada', on_delete=models.CASCADE)
    