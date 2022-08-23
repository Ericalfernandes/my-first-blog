from django import forms # importa o forms do django
from .models import Post, Comment #importa a model Post de models

# Para cada model com um formulário, preciso importa a model aqui

class PostForm(forms.ModelForm): #'PostForm' é o nome do nosso formulário para Post. E 'forms.ModelForm' usamos para informar para o django que vamos usar o padrão de formulário do proprio django

    title = forms.CharField(  # defini um novo tipo de campo para text
    required=True,
    widget=forms.TextInput
  )
    text = forms.CharField(  # defini um novo tipo de campo para text
    required=True,
    widget=forms.Textarea
  )

    class Meta: 
        model = Post #informando para o django a model que será utilizada para criar o formulário
        fields = ['title', 'text']  #especificação dos campos deste formulário

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
