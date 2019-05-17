from django import forms
from .models import Stok, Inventori

class NewStokForm(forms.ModelForm):
    stok = forms.CharField(
        help_text='The max length of the text is 30.'
    )
    
    class Meta:
        model = Stok
        fields = ['stok']

class NewInventoriForm(forms.ModelForm):
    inventori = forms.CharField(
        help_text='The max length of the test is 30.'
    )

    class Meta:
        model = Inventori
        fields = ['inventori', 'harga', 'kuantiti']