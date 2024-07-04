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
import requests
import csv
import os
import subprocess
import pyarrow as pa
import pyarrow.fs as fs
# from hdfs import InsecureClient

kst = pendulum.timezone("Asia/Seoul")

dag = DAG(
    dag_id = 'subway_load',
    description="subway_test",
    start_date=datetime(2024, 7,1, tzinfo=kst),
    schedule_interval="*/5 0 * * *",
    catchup=False,
)

#1  
def get_info_realtime():
    url = 'http://swopenapi.seoul.go.kr/api/subway/6a704b554e6b73653638687a4a6747/json/realtimeStationArrival/ALL/1/5'
    r = requests.get(url).json()
    data = pd.json_normalize(r,record_path=['realtimeArrivalList'])
    filtered_data = {key: r['errorMessage'][key] for key in ['status', 'code', 'message']}
    mes = pd.DataFrame([filtered_data])  
    sample = data[['subwayId','statnNm','arvlMsg2','arvlMsg3','arvlCd','barvlDt','bstatnNm','updnLine','lstcarAt']]
    sample['subwayId'] = sample['subwayId'].astype(int)
    sample = sample[(sample['subwayId'] > 1000) & (sample['subwayId'] < 1010)].sort_values(by='subwayId', ascending=True)
    for col in mes.columns:
        sample[col] = mes[col].iloc[0]
    return sample
    

#load_realtime_position
def get_info_position():
    arrive = pd.DataFrame()
    for i in range(1, 10):
        url = f'http://swopenapi.seoul.go.kr/api/subway/7874454f7a637733313033434a626b61/json/realtimePosition/0/1000/{i}호선'
        r = requests.get(url).json()
        data = pd.json_normalize(r, record_path=['realtimePositionList'])
        filtered_data = {key: r['errorMessage'][key] for key in ['status', 'code', 'message']}
        mes = pd.DataFrame([filtered_data])
        sample = data[['subwayId', 'statnId', 'statnNm','updnLine']]
        sample['subwayId'] = sample['subwayId'].astype(int)
        sample = sample[(sample['subwayId'] > 1000) & (sample['subwayId'] < 1009)].sort_values(by='subwayId', ascending=True)
        for col in mes.columns:
            sample[col] = mes[col].iloc[0]
        arrive = pd.concat([arrive, sample], ignore_index=True)
    return arrive

#2
def merge_send2kafka():
    realtime = get_info_realtime()
    position = get_info_position()
    merged_df = pd.merge(realtime, position, on=['subwayId', 'statnNm'], suffixes=('', '_realtime'), how='inner')
    merged_df.drop_duplicates(subset = 'arvlMsg2', keep = 'first', inplace = True)
    sub_Nm = {
    '1001' : '1호선',
    '1002' : '2호선',
    '1003' : '3호선',
    '1004' : '4호선',
    '1005' : '5호선',
    '1006' : '6호선',
    '1007' : '7호선',
    '1008' : '8호선',}
    arr_cd = {
    '0' : '진입',
    '1' : '도착',
    '2' : '출발',
    '3' : '전역출발',
    '4' : '전역진입',
    '5' : '전역도착',
    '99' : '운행중'}
    
    updnLine_Nm = {
        '0' : '상행/내선',
        '1' : '하행/외선'
    }
    
    for i,k in sub_Nm.items():
        merged_df['subwayId'] = merged_df['subwayId'].astype(str).apply(lambda x : x.replace(i,k))
    for l,m in arr_cd.items():
        merged_df['arvlCd'] = merged_df['arvlCd'].astype(str).apply(lambda x : x.replace(l,m))
    for j,n in updnLine_Nm.items():
        merged_df['updnLine'] = merged_df['updnLine'].astype(str).apply(lambda x : x.replace(j,n))
        
    return merged_df.to_csv('/home/hadoop/workspace/realtime_subway.csv', index = False, encoding = 'utf-8-sig')

def save2Hadoop():
    classpath = subprocess.Popen(["/home/hadoop/hadoop/bin/hdfs", "classpath", "--glob"], stdout=subprocess.PIPE).communicate()[0]
    os.environ["CLASSPATH"] = classpath.decode("utf-8")
    hdfs = fs.HadoopFileSystem(host='192.168.0.160', port=8020, user='hadoop')
    df = pd.read_csv('/home/hadoop/workspace/realtime_subway.csv', encoding='utf-8-sig')
    hdfs_path = '/subway_project/subway_data.csv'
    with hdfs.open_output_stream(hdfs_path) as f:
        df.to_csv(f, index=False)

 
first_load = PythonOperator(task_id='first_load',
                python_callable= get_info_realtime,
                dag=dag
              )

second_load = PythonOperator(task_id = 'second_data',
                           python_callable = get_info_position,
                           dag = dag)

merge_data = PythonOperator(task_id = 'merge_data',
                             python_callable = merge_send2kafka,
                             dag = dag)

send_data = PythonOperator(task_id = 'send_data',
                             python_callable = save2Hadoop,
                             dag = dag)

first_load >> second_load >> merge_data >> send_data
