from django import forms
from .models import Post
# from wow(원래는 wow였는데 내가 move해서 ch3로 수정함).posts import models

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'