from django import forms

class DiaryForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)