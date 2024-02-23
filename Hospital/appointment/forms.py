from django import forms
from .models import PatientModel

class PatientForm(forms.ModelForm):
    class Meta:
        model = PatientModel
        fields = '__all__'