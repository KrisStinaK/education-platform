from django.urls import path
from .views import CourseCreateView
from . import views

app_name = 'courses'

urlpatterns = [
    path('create/', CourseCreateView.as_view(), name='course_create'),
    path('create/lesson', views.create_lesson_view, name='lesson_create'),
    path('list/', views.course_list, name='course_list'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/lesson/<int:lesson_id>/', 
         views.lesson_detail, name='lesson_detail'),
    path('', views.home, name='home'),
    path('course/<int:course_id>/lesson/<int:lesson_id>/delete/', views.lesson_delete_view, name='lesson_delete'),
    path('course/<int:course_id>/lesson/<int:lesson_id>/edit/', views.edit_lesson_view, name='lesson_edit'),
]