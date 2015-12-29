from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from pisobarato.models import Piso
 
 
class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }

class AddPisoForm(ModelForm):
    class Meta:
        model = Piso
        fields = ['titulo', 'tipo', 'lat','lng','descripcion','direccion','fecha_registro','precio']
        widgets = {
			'tipo': forms.RadioSelect(),
            'fecha_registro':forms.DateInput(attrs={'class': 'datepicker'})
         }