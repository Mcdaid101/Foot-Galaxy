from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = {'name', 'stars', 'content'}
        widgets = {
            'content': forms.TextInput(attrs={'style': 'max-height:200px'}),
        }