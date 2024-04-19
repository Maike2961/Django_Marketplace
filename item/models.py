from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        ordering = ('nome',)
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.nome
    
class Item(models.Model):
    categoria = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    preco = models.FloatField()
    imagem = models.ImageField(upload_to='images', blank=True, null=True)
    a_venda = models.BooleanField(default=False)
    criado_por = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome