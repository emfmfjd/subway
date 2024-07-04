# websocket url 라우팅 정의
# WebSocket 연결이 /ws/train-location/ URL로 들어오면 TrainLocationConsumer가 처리
# Django Channels가 WebSocket 요청을 올바른 consumer로 라우팅할 수 있게 함

from django.urls import path
from . import consumer

websocket_urlpatterns = [
    path('ws/train-location/', consumer.TrainLocationConsumer.as_asgi()),
]