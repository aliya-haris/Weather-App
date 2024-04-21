from django import forms
from .models import Weather

class weatherForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields = ['city']