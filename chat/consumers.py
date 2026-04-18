# import json
# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer
# from django.utils import timezone


# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.user = self.scope['user']
#         self.room_id = self.scope['url_route']['kwargs']['room_id']
#         self.room_group_name = f'chat_{self.room_id}'
#         # join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name, self.channel_name
#         )
#         # accept connection
#         self.accept()



#     def disconnect(self, close_code):
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name, self.channel_name
#         )
#     # receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#         now = timezone.now()
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message,
#                 'user': self.user.username,
#                 'datetime': now.isoformat(),
#             }
#         )

#     # receive message from room group
#     def chat_message(self, event):
#         # send message to WebSocket
#         self.send(text_data=json.dumps(event))


import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import ChatMessage, ChatRoom
from courses.models import Course

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f'chat_{self.room_id}'

        # Присоединение к группе
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        # Загрузка последних сообщений
        await self.load_messages()

    async def disconnect(self, close_code):
        # Выход из группы
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Сохранение сообщения в БД
        await self.save_message(self.scope['user'], self.room_id, message)

        # Отправка сообщения всем в группе
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.scope['user'].username,
                'user_id': self.scope['user'].id,
                'timestamp': await self.get_current_time()
            }
        )

    async def chat_message(self, event):
        # Отправка сообщения WebSocket клиенту
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username'],
            'user_id': event['user_id'],
            'timestamp': event['timestamp']
        }))

    @database_sync_to_async
    def save_message(self, user, room_id, message):
        room = ChatRoom.objects.get(id=room_id)
        ChatMessage.objects.create(
            room=room,
            user=user,
            content=message
        )

    async def load_messages(self):
        messages = await self.get_last_messages(self.room_id, 50)
        await self.send(text_data=json.dumps({
            'type': 'load_messages',
            'messages': messages
        }))

    @database_sync_to_async
    def get_last_messages(self, room_id, limit):
        messages = ChatMessage.objects.filter(room_id=room_id).order_by('-timestamp')
        messages = messages.order_by('timestamp')

        return [
            {
                'id': msg.id,
                'content': msg.content,
                'username': msg.user.username,
                'user_id': msg.user.id,
                'timestamp': msg.timestamp.isoformat(),
                'avatar': msg.user.profile.image.url if msg.user.profile.image else ''
            }
            for msg in messages
        ]

    @database_sync_to_async
    def get_current_time(self):
        from django.utils import timezone
        return timezone.now().isoformat()