# websocket 소비자를 정의하여 클라이언트와 실시간 통신 관리
# kafka consumer로부터 데이터를 받아 websocket을 통해 클라이언트로 전송

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from kafka import KafkaConsumer
import asyncio

class TrainLocationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # WebSocket 연결을 수락
        await self.accept()
        
        # Kafka consumer를 설정 -> kafka consumer를 설정하여 지정된 토픽에서 메시지 수신
        self.consumer = KafkaConsumer(
            'train_location_topic',  # Kafka 토픽 이름
            bootstrap_servers=['your_kafka_server:9092'],  # Kafka 서버 주소
            auto_offset_reset='earliest',  # 시작 오프셋 설정
            enable_auto_commit=True,  # 자동 커밋 활성화
            group_id='train-location-group',  # consumer 그룹 ID
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # 메시지 디코딩 설정
        )
        
        # 비동기로 메시지를 처리
        asyncio.create_task(self.consume_messages())

    async def disconnect(self, close_code):
        # WebSocket 연결이 닫힐 때 Kafka consumer 닫기
        self.consumer.close()

    async def consume_messages(self):
        # Kafka 메시지를 수신하고 WebSocket을 통해 클라이언트로 전송
        for message in self.consumer:
            data = message.value
            await self.send(json.dumps(data))
