"""
ASGI config for mini3 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

# For Channels routing
# ProtocolTypeRouter를 사용하여 HTTP 및 WebSocket 프로토콜을 처리
# HTTP 요청은 get_asgi_application을 통해 처리
# WebSocket 요청은 AuthMiddlewareStack을 통해 인증되고 URLRouter를 통해 라우팅
# websocket_urlpatterns를 사용하여 WebSocket 요청을 TrainLocationConsumer로 라우팅


import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from subway.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mini3.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})