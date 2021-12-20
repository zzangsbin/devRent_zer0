from django import forms
from .models import Post

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = '__all__'

     #포스트 모델에 있는 모든 필드로 나느폼을 만들거야