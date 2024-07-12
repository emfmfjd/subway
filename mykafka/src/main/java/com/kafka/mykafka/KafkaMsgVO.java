package com.kafka.mykafka;

import lombok.Data;

@Data
public class KafkaMsgVO {
	private String subwayNm;
	private Integer trainNo;
    private String statnNm;
    private String statnTnm;
    private Integer trainSttus;
    private String updnLine;
    private Integer status;
    private String code;
    private String message;
}