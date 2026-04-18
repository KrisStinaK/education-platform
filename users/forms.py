from django import forms
from .models import Profile
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):  
    username = forms.CharField(max_length=50, label='Имя пользователя (username)')  
    class Meta:  
        model = User  
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image', 'bio']
		

