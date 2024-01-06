from django import forms
from .models import Price

class Price(forms.ModelForm):
    
    class Meta:
        model = Price
        fields = ('name', 'totsp', 'livesp', 'kitsp', 'dist', 'metrdist', 'walk', 'brick', 'floor')