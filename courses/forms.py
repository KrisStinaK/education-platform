from django import forms
from .models import Lesson, CourseProgress, Course
from django.contrib.auth.models import User


class LessonUpdateForm(forms.ModelForm):
	class Meta:
		model = Lesson
		fields = ['course', 'title', 'content',
			 'images', 'file', 'url', 'order', 'is_published']
		

class CourseProgressForm(forms.ModelForm):
    class Meta:
        model = CourseProgress
        fields = ['student', 'course', 'completed_lessons'] 
