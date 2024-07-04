from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TrainData
from .serializers import TrainDataSerializer

# Create your views here.

@api_view(['POST'])
def train_data(request):
    if request.method == 'POST':
        serializer = TrainDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def line1(request):
    return render(request, 'subway/line1.html')

def line2(request):
    return render(request, 'subway/line2.html')

def line3(request):
    return render(request, 'subway/line3.html')

def line4(request):
    return render(request, 'subway/line4.html')

def line5(request):
    return render(request, 'subway/line5.html')

def line6(request):
    return render(request, 'subway/line6.html')

def line7(request):
    return render(request, 'subway/line7.html')

def line8(request):
    return render(request, 'subway/line8.html')

def index(request):
    return render(request, 'subway/line1.html')

