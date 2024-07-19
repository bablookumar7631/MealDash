from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

from .models import Profile
from django.forms.models import ModelForm
from django.forms.widgets import FileInput



class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'placeholder':'Email Address'}))

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'

		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'



class ProfileForm(ModelForm):
	class Meta:
		models = Profile
		fields = '__all__'
		exclude = ['user']
		widgets = {
			'profile_img': FileInput(),
			'mobile_no':  forms.NumberInput()
		}
