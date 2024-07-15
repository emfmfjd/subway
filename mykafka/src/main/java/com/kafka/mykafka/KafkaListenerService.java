package com.kafka.mykafka;

import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class KafkaListenerService {

    @KafkaListener(topics = "subway_pos", containerFactory = "kafkaListenerContainerFactory")
    public void listen(KafkaMsgVO message) {
        System.out.println("Received message: " + message);
    }
}