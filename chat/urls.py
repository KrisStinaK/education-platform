from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_rooms, name='chat_rooms'),
    path('room/<int:room_id>/', views.chat_room, name='chat_room'),
    path('send/<int:room_id>/', views.send_message, name='send_message'),
    path('send/<int:room_id>/', views.send_message, name='send_message'),
]