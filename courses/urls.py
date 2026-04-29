from django.urls import path
from .views import CourseCreateView
from . import views

app_name = 'courses'

urlpatterns = [
    path('create/', CourseCreateView.as_view(), name='course_create'), # URL для создания курса
    path('create/lesson', views.create_lesson_view, name='lesson_create'), # URL для создания урока
    path('list/', views.course_list, name='course_list'), # URL для просмотра списка курсов
    path('course/<int:pk>/', views.course_detail, name='course_detail'), # URL для детального просмотра курса
    path('course/<int:course_id>/lesson/<int:lesson_id>/', 
         views.lesson_detail, name='lesson_detail'), # URL для детального просмотра урока
    path('', views.home, name='home'), # URL для домашней страницы
    path('course/<int:course_id>/lesson/<int:lesson_id>/delete/', views.lesson_delete_view, name='lesson_delete'), # URL для удаления урока
    path('course/<int:course_id>/lesson/<int:lesson_id>/edit/', views.edit_lesson_view, name='lesson_edit'), # URL для редактирования урока
    # path('enroll/<int:course_id>/', views.enroll, name='enroll'),
    path('<int:course_id>/analytics/', views.course_analytics, name='course_analytics'), # URL для аналитики
    path('lesson_complete/<int:lesson_id>/', views.mark_lesson_complete, name='mark_lesson_complete'), # URL для отметки урока как завершенного

]
