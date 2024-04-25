from django.contrib import admin

from .models import Conversation, ConversationMessage

@admin.register(Conversation)
class ConversationShow(admin.ModelAdmin):
    list_display=('item','relaciona_objeto' ,'criado_em', 'modificado_em')
    
    def relaciona_objeto(self, obj):
        return ", ".join([str(membro) for membro in obj.membros.all()])
    
@admin.register(ConversationMessage)
class ConversationMessageShow(admin.ModelAdmin):
    list_display = ('conversa', 'content', 'criado_em', 'criado_por')
    
