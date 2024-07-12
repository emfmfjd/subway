import json
import pandas as pd
import requests
import pendulum
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from confluent_kafka import Producer
import subprocess
import os
from pyarrow import fs
import fsspec

kst = pendulum.timezone("Asia/Seoul")

dag = DAG(
    dag_id='subway_project',
    description="save2hadoop",
    start_date=datetime(2024, 7, 5, tzinfo=kst),
    schedule_interval="*/1 09 * * *",
    catchup=False,
)

def get_info_position():
    arrive = pd.DataFrame()
    url = 'http://swopenapi.seoul.go.kr/api/subway/7874454f7a637733313033434a626b61/json/realtimePosition/0/1000/3호선'
    r = requests.get(url).json()
    data = pd.json_normalize(r, record_path=['realtimePositionList'])
    filtered_data = {key: r['errorMessage'][key] for key in ['status', 'code', 'message']}
    mes = pd.DataFrame([filtered_data])
    sample = data[['subwayNm', 'trainNo', 'statnNm', 'statnTnm', 'trainSttus', 'updnLine']]
    for col in mes.columns:
        sample[col] = mes[col].iloc[0]
    arrive = pd.concat([arrive, sample], ignore_index=True)
    return arrive

def processing_data():
    position = get_info_position()
    
    sub_Nm = {
        '1001': '1호선',
        '1002': '2호선',
        '1003': '3호선',
        '1004': '4호선',
        '1005': '5호선',
        '1006': '6호선',
        '1007': '7호선',
        '1008': '8호선',
    }
    train_stat = {
        '0': '진입',
        '1': '도착',
        '2': '출발',
        '3': '전역출발',
    }
    updnLine_Nm = {
        '0': '상행/내선',
        '1': '하행/외선'
    }

    # 데이터 전처리
    position['updnLine'] = position['updnLine'].astype(str).replace(updnLine_Nm)
    position['trainSttus'] = position['trainSttus'].astype(str).replace(train_stat)
    
    # JSON 파일로 저장
    position.to_json('/home/hadoop/project_data/realtime_position.json', force_ascii=False, orient='records')

def save2Hadoop():
    classpath = subprocess.Popen(["/home/hadoop/hadoop/bin/hdfs", "classpath", "--glob"], stdout=subprocess.PIPE).communicate()[0]
    os.environ["CLASSPATH"] = classpath.decode("utf-8")
    hdfs = fs.HadoopFileSystem(host='192.168.0.211', port=8020, user='hadoop')
    df = pd.read_json('/home/hadoop/project_data/realtime_position.json', encoding='utf-8-sig')
    hdfs_path = 'hdfs://192.168.0.211:8020/subway_project/subway_position.json'
    with fsspec.open(hdfs_path, 'w', encoding='utf-8', user='hadoop') as f:
        df.to_json(f, force_ascii=False, orient='records')

get_info_position_task = PythonOperator(
    task_id='get_info_position',
    python_callable=get_info_position,
    dag=dag,
)

processing_data_task = PythonOperator(
    task_id='processing_data',
    python_callable=processing_data,
    dag=dag,
)

save_data_task = PythonOperator(
    task_id='save_data',
    python_callable=save2Hadoop,
    dag=dag,
)

get_info_position_task >> processing_data_task >> save_data_task