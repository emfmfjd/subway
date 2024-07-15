package com.kafka.mykafka;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.kafka.annotation.EnableKafka;
import org.springframework.kafka.config.ConcurrentKafkaListenerContainerFactory;
import org.springframework.kafka.core.ConsumerFactory;
import org.springframework.kafka.core.DefaultKafkaConsumerFactory;

import org.springframework.kafka.support.serializer.ErrorHandlingDeserializer;
import org.springframework.kafka.support.serializer.JsonDeserializer;
import org.springframework.beans.factory.annotation.Value;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.common.serialization.StringDeserializer;


import java.util.HashMap;
import java.util.Map;

@EnableKafka
@Configuration
public class KafkaConfig {
    @Value("${spring.kafka.bootstrap-servers}")
    private String servers;

    @Bean
public ConsumerFactory<String, KafkaMsgVO> consumerFactory() {
    Map<String, Object> props = new HashMap<>();
    props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, servers);
    props.put(ConsumerConfig.GROUP_ID_CONFIG, "subway_con");
    props.put(JsonDeserializer.TRUSTED_PACKAGES, "com.kafka.mykafka");
    props.put(JsonDeserializer.VALUE_DEFAULT_TYPE, "com.kafka.mykafka.KafkaMsgVO");
    props.put(ConsumerConfig.MAX_POLL_RECORDS_CONFIG, 50);

    JsonDeserializer<KafkaMsgVO> deserializer = new JsonDeserializer<>(KafkaMsgVO.class);
    deserializer.configure(props, false);

    return new DefaultKafkaConsumerFactory<>(
            props,
            new ErrorHandlingDeserializer<>(new StringDeserializer()),
            new ErrorHandlingDeserializer<>(deserializer)
    );
}

@Bean
public ConcurrentKafkaListenerContainerFactory<String, KafkaMsgVO> kafkaListenerContainerFactory() {
    ConcurrentKafkaListenerContainerFactory<String, KafkaMsgVO> factory = new ConcurrentKafkaListenerContainerFactory<>();
    factory.setConsumerFactory(consumerFactory());
    return factory;
}
}
