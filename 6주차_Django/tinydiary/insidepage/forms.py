from django import forms
from .models import Diary, Comment

class DiaryModelForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'create__input'
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'class': 'create__textarea',
                }
            )
        }

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'create__input'
            })
        }