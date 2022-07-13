from django import forms
from .models import Diary, Comment

class DiaryForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
        'class': 'create__input'
    }))
    body = forms.CharField(
        widget=forms.Textarea(attrs={
        'class': 'create__textarea'
    }))

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'create__input'
            })
        }