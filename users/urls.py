from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
 path("signup/", views.SignUp.as_view(), name="signup"),
 path('', views.profile_view, name='profile'),
 path('edit', views.edit_profile, name='edit_profile'),
]