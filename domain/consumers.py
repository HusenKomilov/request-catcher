import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class DomainConsumer(WebsocketConsumer):
    def connect(self):
        self.domain = self.scope['url_route']['kwargs']['domain']
        async_to_sync(self.channel_layer.group_add)(self.room_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.room, self.channel_name)

    def chat_message(self, event):
        message = event["message"]
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))

# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync

# def sendDeployments(owner, armies):
#     type = "renderDeployments"
#     message = owner + " has " + str(armies) + " to deploy"
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#         'render_updates_group',
#         {'type': 'render', 'message': message}
#     )