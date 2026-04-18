from django.contrib import admin
from .models import Answer, Quiz, Question, Result

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Result)