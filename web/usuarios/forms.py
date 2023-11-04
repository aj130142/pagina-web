from django import forms
from django.forms import  ModelForm
from .models import Cliente, medico, contacto

class formCliente (ModelForm):
    Nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}), 
        input_formats=['%Y-%m-%d'],
    )
    Fecha_Actual = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}), 
        input_formats=['%Y-%m-%d'],
    )

    class Meta:
        model = Cliente
        fields = '__all__'
        
class formMedico (ModelForm):
    
    class Meta:
        model = medico
        fields = '__all__'

class formContacti (ModelForm):

    class Meta:
        model = contacto
        fields = '__all__'