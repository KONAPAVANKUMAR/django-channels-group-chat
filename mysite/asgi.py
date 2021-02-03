import os

from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
import chat.consumers
from django.urls import path
from channels.auth import AuthMiddlewareStack
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
    "websocket" : AuthMiddlewareStack(URLRouter([path('ws/chat/<int:room_name>/',chat.consumers.ChatConsumer.as_asgi())]))
})