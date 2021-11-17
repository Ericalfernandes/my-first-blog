from django.shortcuts import render
from django.utils import timezone #precisei importar para usar o timezone (da query)
from .models import Post #importando a model Post de models.py

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #adicionei a query e atribui o valor dela a uma variavel
    return render(request, 'blog/post_list.html', {'posts':posts}) #adicionei parametros para que eu possa mandar esses valores da query p template

