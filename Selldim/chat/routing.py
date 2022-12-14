from django.urls import re_path, path
from Selldim.chat import consumers as chat_consumers


websocket_url_patterns = [
    path('ws/chat/<room_name>/<str:username>/', chat_consumers.ChatRoomConsumer.as_asgi()),
]
