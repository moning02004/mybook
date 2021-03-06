from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DashConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.my_username = self.scope['url_route']['kwargs']['my_username']

        # Join room group
        await self.channel_layer.group_add(
            self.my_username,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.my_username,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        # Send message to room group
        await self.channel_layer.group_send(
            self.my_username,
            {
                'type': 'chat_message',
                'message': ''
            }
        )

    # Receive message from room group
    async def refresh(self, event):
        await self.send(text_data=json.dumps({
            'last_message': event['content'],
            'user': event['user'],
            'unread': event['unread']

        }))