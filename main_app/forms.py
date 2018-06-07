from django import forms
from .models import Trip
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TripForm(forms.ModelForm):
	
	class Meta:
		model = Trip
		fields = ['destination', 'duration', 'languages', 'climate', 'items_needed']

class LoginForm(forms.Form):
	username = forms.CharField(label="User Name", max_length=70)
	password = forms.CharField(widget=forms.PasswordInput())

class SignupForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    email = forms.EmailField(max_length=200, help_text='Required')
    password = forms.CharField(widget=forms.PasswordInput())