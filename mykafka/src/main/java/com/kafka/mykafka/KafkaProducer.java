package com.kafka.mykafka;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

@Service
public class KafkaProducer {
    private static final String TOPIC = "subway";
    private final KafkaTemplate<String, KafkaMsgVO> kafkaTemplate;

    @Autowired
    public KafkaProducer(KafkaTemplate<String, KafkaMsgVO> kafkaTemplate) {
	this.kafkaTemplate = kafkaTemplate;
    }

    public void sendMessage(KafkaMsgVO message) {
        System.out.println(String.format("Produce message(KafkaMsgVO) : %s", message));
        this.kafkaTemplate.send(TOPIC, message);
    }
}