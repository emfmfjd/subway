package com.kafka.mykafka;

import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class KafkaConsumer {
@KafkaListener(topics = "subway", groupId = "subway_con")
    public void consume(KafkaMsgVO vo){
        System.out.println("SubwayNm = " + vo.getSubwayNm());
        System.out.println("TrainNo = " + vo.getTrainNo());
        System.out.println("StatnNm = " + vo.getStatnNm());
        System.out.println("StatnTnm = " + vo.getStatnTnm());
        System.out.println("TrainSttus = " + vo.getTrainSttus());
        System.out.println("UpdnLine = " + vo.getUpdnLine());
        System.out.println("Status = " + vo.getStatus());
        System.out.println("Code = " + vo.getCode());
        System.out.println("Message = " + vo.getMessage());
    }
}