"WebSocket for Course model"

import json

from channels.generic.websocket import AsyncWebsocketConsumer

class CourseConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("course_creates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("course_creates", self.channel_name)

    async def course_created(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
