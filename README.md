# 에어플로우 airflow

## task

- get_info
    - 실시간 위치, 주소, get방식으로 받아옴 → df로 변경
- processing_data
    - 간단한 매핑 전처리 → json파일로 로컬 저장
- load_jaon_to_db
    - json파일을 장고 db에 올림
- kafka_producer_function
    - 로컬에 있는 걸 열어서 json으로 받아서 읽음 → 카프카 프로듀서로 보냄
    - conf → 카프카 클러스터 설정
    

# 카프카

## task

- producer에서 보낸 consumer 받아오는 파일
- airflow에서 json 형식으로 만든 데이터를 hadoop으로 저장

# 장고

## task

- 호선 별로 페이지 옮기기
- 마커(열차) 움직이게 하기

# 4차 프로젝트

## to do

- 새로 hadoop 서버 구축하여 사용

- airflow에서 받아온 데이터를 스프링부트로 넘기기
    
    try1. json 형태로 데이터를 받아와서 카프카에서 스프링부트로 보내기
    
    try2. 하둡에서 스프링부트로 보내기
    
- airlfow에서 하둡과 카프카로 병렬처리 구현
