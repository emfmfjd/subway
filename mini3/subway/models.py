from django.db import models

class TrainData(models.Model):
    line = models.CharField(max_length=100)  # 호선
    station = models.CharField(max_length=100)  # 역명
    destination = models.CharField(max_length=100)  # 종착역
    status = models.CharField(max_length=100)  # 열차 상태구분
    direction = models.CharField(max_length=10)  # 상하행구분
    arrival_time = models.DateTimeField()  # 데이터 저장 시간

    def __str__(self):
        return f"{self.line} - {self.station} - {self.status}"
