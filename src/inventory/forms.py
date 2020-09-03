from django import forms
from .models import *


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ('type', 'price', 'status', 'issues',)


class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = ('type', 'price', 'status', 'issues',)


class MobilesForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ('type', 'price', 'status', 'issues',)
