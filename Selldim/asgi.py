"""
ASGI config for Selldim project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from Selldim.chat import routing as chat_routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Selldim.settings')
# django_asgi_app = get_asgi_application()
# application = get_asgi_application()

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
