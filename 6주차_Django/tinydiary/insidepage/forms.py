from django import forms
from .models import Diary

class DiaryModelForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'body']
        title = forms.CharField(
            widget=forms.TextInput(attrs={
            'class': 'create__input'
        }))
        body = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'create__textarea'
        }))

