from django.urls import path
from . import views

app_name = 'certificates'

urlpatterns = [
    path('issue/<int:course_id>/', views.issue_certificate, name='issue_certificate'),
    path('detail/<str:certificate_number>/', views.certificate_detail, name='certificate_detail'),
]