from django import forms
from .models import Lesson, CourseProgress, Course, Comment
from django.contrib.auth.models import User


class LessonUpdateForm(forms.ModelForm):
	class Meta:
		model = Lesson
		fields = ['course', 'title', 'description', 'is_published',
            'order']
		

class CourseProgressForm(forms.ModelForm):
    class Meta:
        model = CourseProgress
        fields = ['student', 'course', 'completed_lessons'] 


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']