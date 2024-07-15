package com.kafka.mykafka;

import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class KafkaConsumer {
@KafkaListener(topics = "subway_pos", groupId = "subway_con1")
    public void consume(KafkaMsgVO vo){
        System.out.println("SubwayNm = " + vo.getSubwayNm()); // 지하철호선명(3호선)
        System.out.println("TrainNo = " + vo.getTrainNo()); // 열차번호(3165)
        System.out.println("StatnNm = " + vo.getStatnNm()); // 지하철역명(구파발)
        System.out.println("StatnTnm = " + vo.getStatnTnm()); // 종착지하철역명(오금)
        System.out.println("TrainSttus = " + vo.getTrainSttus()); // 열차상태구분(진입, 도착, 출발, 전역출발)
        System.out.println("UpdnLine = " + vo.getUpdnLine()); // 상하행선구분(상행/내선, 하행/외선)
        System.out.println("Status = " + vo.getStatus()); // 처리 상태 번호(200)
        System.out.println("Code = " + vo.getCode()); // 처리 메시지 코드(INFO-000)
        System.out.println("Message = " + vo.getMessage()); // 처리 메시지(정상 처리되었습니다.)
    }
}
