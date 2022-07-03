from django import forms

class DiaryForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
        'class': 'create__input'
    }))
    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'create__textarea'
    }))

