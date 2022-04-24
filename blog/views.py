from django.utils import timezone #precisei importar para usar o timezone (da query)
from .models import Post, Comment #importando a model Post de models.py
from django.shortcuts import render, get_object_or_404, redirect #rdirecionar para outra view, página
from .forms import PostForm, CommentForm

# Create your views here.
#Comments functions
def comment(request): #criei temporariamente, para conseguir ver todos os objetos de comment
    comment = Comment.objects.all().order_by('created_date')
    return render(request, 'blog/comment_detail.html', {'comment':comment}) #mudança p renderizar o htmal de detail dos posts

def comment_new(request):
        if request.method == "POST": #condição para salvar os dados do form quando houver dados
            form = CommentForm(request.POST) #request.POST estamos enviando dados, vem do método POST
        if form.is_valid(): #checar se o formulário está correto (todos os campos requeridos estão prontos e valores incorretos não serão salvos)
            post = form.save(commit=False) #significa que não queremos salvar o model de Post ainda
            post.author = request.user
            post.created_date = timezone.now()
            post.save() #vai preservar as alterações (adicionando o autor) e é criado um novo post no blog
            return redirect('post_detail', pk=post.pk)
        else:
            form = CommentForm() #senão renderiza o proprio form vazio
        return render(request, 'blog/post_detail.html', {'form': form})

# Post functions

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #adicionei a query e atribui o valor dela a uma variavel
    return render(request, 'blog/post_list.html', {'posts':posts}) #adicionei parametros para que eu possa mandar esses valores da query p template

def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk) #nova query
    comment = Comment.objects.filter(post_id=pk)
    return render(request, 'blog/post_detail.html', {'post':posts, 'comment':comment}) #mudança p renderizar o html de detail dos posts

def post_new(request):
    if request.method == "POST": #condição para salvar os dados do form quando houver dados
        form = PostForm(request.POST) #request.POST estamos enviando dados, vem do método POST
        if form.is_valid(): #checar se o formulário está correto (todos os campos requeridos estão prontos e valores incorretos não serão salvos)
            post = form.save(commit=False) #significa que não queremos salvar o model de Post ainda
            post.author = request.user
            post.published_date = timezone.now()
            post.save() #vai preservar as alterações (adicionando o autor) e é criado um novo post no blog
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm() #senão renderiza o proprio form vazio
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


