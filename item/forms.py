from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class novoItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('categoria', 'nome', 'descricao', 'preco', 'imagem')
        widgets = {
            'categoria': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'nome': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'descricao': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'preco': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'imagem': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }
class EditaItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('nome', 'descricao', 'preco', 'imagem', 'a_venda')
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'descricao': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'preco': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'imagem': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }