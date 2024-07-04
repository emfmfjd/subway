import json
import pathlib
import airflow.utils.dates
import requests
import requests.exceptions as requests_exceptions
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pendulum
import os
import pandas as pd
import csv
import subprocess
import pyarrow as pa
import pyarrow.fs as fs
from hdfs import InsecureClient
from confluent_kafka import Producer
# from airflow.providers.apache.kafka.operators.produce_to_topic
# import ProduceToTopicOperator
from airflow import DAG
# from airflow_provider_kafka.operators.consume_from_topic import ConsumeFromTopicOperator
# from airflow_provider_kafka.operators.produce_to_topic import ProduceToTopicOperator


kst = pendulum.timezone("Asia/Seoul")

dag = DAG(
    dag_id = 'subway_load',
    description="subway_test",
    start_date=datetime(2024, 7,1, tzinfo=kst),
    schedule_interval="*/5 0 * * *",
    catchup=False,
)


#load_realtime_position
def get_info_position():
    arrive = pd.DataFrame()
    url = 'http://swopenapi.seoul.go.kr/api/subway/7874454f7a637733313033434a626b61/json/realtimePosition/0/1000/3호선'
    r = requests.get(url).json()
    data = pd.json_normalize(r, record_path=['realtimePositionList'])
    filtered_data = {key: r['errorMessage'][key] for key in ['status', 'code', 'message']}
    mes = pd.DataFrame([filtered_data])
    sample = data[['subwayNm', 'statnNm', 'statnTnm', 'trainSttus', 'updnLine']]
    for col in mes.columns:
        sample[col] = mes[col].iloc[0]
    arrive = pd.concat([arrive, sample], ignore_index=True)
    return arrive

#2
def processing_data():
    position = get_info_position()
    sub_Nm = {
    '1001' : '1호선',
    '1002' : '2호선',
    '1003' : '3호선',
    '1004' : '4호선',
    '1005' : '5호선',
    '1006' : '6호선',
    '1007' : '7호선',
    '1008' : '8호선',}
    train_stat = {
    '0' : '진입',
    '1' : '도착',
    '2' : '출발',
    '3' : '전역출발',
    }
    
    updnLine_Nm = {
        '0' : '상행/내선',
        '1' : '하행/외선'
    }
    
    for j,n in updnLine_Nm.items():
        position['updnLine'] = position['updnLine'].astype(str).apply(lambda x : x.replace(j,n))
    for z,c in train_stat.items():
        position['trainSttus'] = position['trainSttus'].astype(str).apply(lambda x : x.replace(z,c))
    #return position.to_csv('/home/hadoop/workspace/realtime_subway.csv', index = False, encoding = 'utf-8-sig')
    with open('/home/hadoop/workspace/realtime_position.json', 'w', encoding='utf-8') as f:
        position.to_json(f, force_ascii=False, orient='records')
    with open('/home/hadoop/workspace/realtime_position.json', 'r') as f:
        data = json.load(f)

###########################################################################################################################
# def kafka_producer_function():
#     conf = {
#         'bootstrap.servers': '192.168.0.209:9092,192.168.0.211:9092,192.168.0.208:9092',
#         'client.id': 'airflowproducer',
#     }
    
#     producer = Producer(conf)
    
#     data = {
#         'str' : 'hello world'
#     }
    
#     message = json.dumps(data)
    
#     topic = 'subway'
    
#     def delivery_report(err, msg):
#         if err is not None:
#             print(f"Message delivery failed: {err}")
#         else:
#             print(f"Message delivered to {msg.topic()} [{msg.partition()}]")
    
#     producer.produce(topic, message.encode('utf-8'), callback=delivery_report)
    
#     producer.flush()

# def save2Hadoop():
#     classpath = subprocess.Popen(["/home/hadoop/hadoop/bin/hdfs", "classpath", "--glob"], stdout=subprocess.PIPE).communicate()[0]
#     os.environ["CLASSPATH"] = classpath.decode("utf-8")
#     hdfs = fs.HadoopFileSystem(host='192.168.0.160', port=8020, user='hadoop')
#     df = pd.read_csv('/home/hadoop/workspace/realtime_subway.csv', encoding='utf-8-sig')
#     hdfs_path = '/subway_project/subway_data.csv'
#     with hdfs.open_output_stream(hdfs_path) as f:
#         df.to_csv(f, index=False)
        
# def send2kafka():
#     pass


position_load = PythonOperator(task_id = 'position_data',
                           python_callable = get_info_position,
                           dag = dag)

processing = PythonOperator(task_id = 'processing_data',
                             python_callable = processing_data,
                             dag = dag)

# send_data = PythonOperator(task_id = 'send_data',
#                              python_callable = save2Hadoop,
#                              dag = dag)

position_load >> processing