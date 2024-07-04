from django.db import models

class TrainData(models.Model):
    # trainNo = models.IntegerField(primary_key=True, null=False)
    subwayNm = models.CharField(max_length=5)
    statnNm = models.CharField(max_length=15)
    updnLine = models.CharField(max_length=5)
    statnTnm = models.CharField(max_length=15)
    trainSttus = models.CharField(max_length=5)
    status = models.IntegerField()
    code = models.TextField(default='INFO-000')
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.trainNo