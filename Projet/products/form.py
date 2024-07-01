from django import forms
from .models import Articles



class ArticleForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea(
        attrs = {
            'placeholder': 'la description ici',
        }
    ))

    class Meta:
        model = Articles
        fields = ['name', 'description', 'price', 'actif', 'slug', 'image']
