from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'price', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter product name'}),
            'quantity': forms.NumberInput(attrs={'min': 0}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
