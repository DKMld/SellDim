import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from Selldim.chat import routing as chat_routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Selldim.settings')

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                chat_routing.websocket_url_patterns
            )
        )
    }
)
