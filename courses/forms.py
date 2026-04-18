from django import forms
from .models import Lesson
from django.contrib.auth.models import User




class LessonUpdateForm(forms.ModelForm):
	class Meta:
		model = Lesson
		fields = ['course', 'title', 'content',
			 'images', 'file', 'url', 'order', 'is_published']
		

