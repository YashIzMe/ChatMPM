import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
#from asgiref.sync import await_to_sync

from chat.models import ChatMessage

class ChatConsumer(AsyncWebsocketConsumer):
    """ handshake websocket front end """

    room_name = None
    room_group_name = None

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        

    async def disconnect(self, code):
        # Leave room group
        if self.room_group_name and self.channel_name:
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': self.scope['user'].username.title(),
                'message': message
            }
        )

        await save_chat_message(
            username=self.scope['user'].username.title(),
            room_id=self.room_name,
            message=message,
        )

        print(message)



    # Receive message from room group
    async def chat_message(self, event):
        """ exhange message here """
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

        print(message + "2")

@database_sync_to_async
def save_chat_message(room_id,username,message):
    return ChatMessage.objects.create(room_id=room_id,username=username,message=message)