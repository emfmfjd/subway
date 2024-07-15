// package com.kafka.mykafka;

// import lombok.Data;

// @Data
// public class KafkaMsgVO {
	// private String subwayNm;
	// private String trainNo;
    // private String statnNm;
    // private String statnTnm;
    // private String trainSttus;
    // private String updnLine;
    // private String status;
    // private String code;
    // private String message;
// }

package com.kafka.mykafka;

public class KafkaMsgVO {
	private String subwayNm;
	private String trainNo;
    private String statnNm;
    private String statnTnm;
    private String trainSttus;
    private String updnLine;
    private String status;
    private String code;
    private String message;
    
    // 기본 생성자
    public KafkaMsgVO() {}

    // 필드를 포함한 생성자
    public KafkaMsgVO(String subwayNm, String trainNo, String statnNm, String statnTnm, String trainSttus, String updnLine, String status, String code, String message) {
        this.subwayNm = subwayNm;
        this.trainNo = trainNo;
        this.statnNm = statnNm;
        this.statnTnm = statnTnm;
        this.trainSttus = trainSttus;
        this.updnLine = updnLine;
        this.status = status;
        this.code = code;
        this.message = message;
    }

    // getter와 setter
    public String getSubwayNm() {
        return subwayNm;
    }

    public void setSubwayNm(String subwayNm) {
        this.subwayNm = subwayNm;
    }

    public String getTrainNo() {
        return trainNo;
    }

    public void setTrainNo(String trainNo) {
        this.trainNo = trainNo;
    }

    public String getStatnNm() {
        return statnNm;
    }

    public void setStatnNm(String statnNm) {
        this.statnNm = statnNm;
    }

    public String getStatnTnm() {
        return statnTnm;
    }

    public void setStatnTnm(String statnTnm) {
        this.statnTnm = statnTnm;
    }

    public String getTrainSttus() {
        return trainSttus;
    }

    public void setTrainSttus(String trainSttus) {
        this.trainSttus = trainSttus;
    }

    public String getUpdnLine() {
        return updnLine;
    }

    public void setUpdnLine(String updnLine) {
        this.updnLine = updnLine;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    @Override
    public String toString() {
        return "KafkaMsgVO{" +
                "subwayNm='" + subwayNm + '\'' +
                ", trainNo='" + trainNo + '\'' +
                ", statnNm='" + statnNm + '\'' +
                ", statnTnm='" + statnTnm + '\'' +
                ", trainSttus='" + trainSttus + '\'' +
                ", updnLine='" + updnLine + '\'' +
                ", status='" + status + '\'' +
                ", code='" + code + '\'' +
                ", message='" + message + '\'' +
                '}';
    }
}