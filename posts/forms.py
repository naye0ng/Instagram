from django import forms
from .models import Post, Comment

# Post라는 모델을 조작할 수 있는 PostModelForm을 정의
class PostModelForm(forms.ModelForm):
    # 1. 어떤 input 필드를 가지는지
    content = forms.CharField(label='',widget=forms.Textarea(attrs={
        'placeholder' : '오늘은 무엇을 하셨나요?'
    }))
    
    # 2. 해당 input
    class Meta :
        model = Post
        fields = ['content','image']


class CommentModelForm(forms.ModelForm):
    class Meta :
        model = Comment
        fields = ['content']