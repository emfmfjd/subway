from django.db import models

class TrainData(models.Model):
    subwayNm = models.CharField(max_length=50)
    trainNo = models.CharField(max_length=50)
    statnNm = models.CharField(max_length=50)
    statnTnm = models.CharField(max_length=50)
    trainSttus = models.CharField(max_length=50)
    updnLine = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    code = models.CharField(max_length=10)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.train_id
    
class RealtimePosition(models.Model):
    subwayNm = models.CharField(max_length=50)
    trainNo = models.CharField(max_length=50)
    statnNm = models.CharField(max_length=50)
    statnTnm = models.CharField(max_length=50)
    trainSttus = models.CharField(max_length=50)
    updnLine = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    code = models.CharField(max_length=10)
    message = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.trainNo} - {self.statnNm}'