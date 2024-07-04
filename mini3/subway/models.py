from django.db import models

# Create your models here.

class TrainData(models.Model):
    train_id = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    arrival_time = models.DateTimeField()

    def __str__(self):
        return self.train_id