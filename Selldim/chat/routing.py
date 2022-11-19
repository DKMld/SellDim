from django.urls import re_path
from Selldim.chat import consumers as chat_consumers


websocket_url_patterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', chat_consumers.ChatRoomConsumer.as_asgi())
]
