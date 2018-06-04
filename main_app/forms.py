from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
	
	class Meta:
		model = Trip
		fields = ['destination', 'duration', 'languages', 'climate', 'items_needed']

class LoginForm(forms.Form):
	username = forms.CharField(label="User Name", max_length=70)
	password = forms.CharField(widget=forms.PasswordInput())