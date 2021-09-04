from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['specialization', 'ssn', 'nation_id', "number", 'city', 'image', 'experience']
class DefaultProfileForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name')

class CreateUserForm(UserCreationForm):
	email = forms.EmailField(required=False)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")