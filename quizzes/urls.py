from django.urls import path
from . import views

app_name = 'quizzes'

urlpatterns = [
    path('list/', views.quiz_list, name='quiz_list'),
    path('create/<int:lesson_id>/', views.quiz_create, name='quiz_create'),
    path('detail/<int:quiz_id>/', views.start_test, name='quiz_detail'),
    path('results/', views.results_history, name='results_history'),
]