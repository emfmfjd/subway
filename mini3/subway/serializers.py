from rest_framework import serializers
from .models import TrainData

class TrainDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainData
        fields = '__all__'