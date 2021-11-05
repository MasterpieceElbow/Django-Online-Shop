from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['owner', 'product', 'body']
        widgets = {'owner': forms.HiddenInput(),
                   'product': forms.HiddenInput(),
                   'body': forms.Textarea(attrs={'rows': 6})}
        labels = {'body': ''}


class SearchForm(forms.Form):
    query = forms.CharField()