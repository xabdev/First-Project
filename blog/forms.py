from django import forms
from .models import Post, Consulta

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image',)

class ConsultaForm(forms.ModelForm):
    
    class Meta:
        model = Consulta
        fields = '__all__'














