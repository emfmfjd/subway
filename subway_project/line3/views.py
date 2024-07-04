from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TrainData
from .serializers import TrainDataSerializer


# Create your views here.

def home_redirect(request):
    return render(request, 'line3/line1.html')

def line1(request):
    return render(request, 'line3/line1.html')

def line2(request):
    return render(request, 'line3/line2.html')

def line3(request):
    return render(request, 'line3/line3.html')

def line4(request):
    return render(request, 'line3/line4.html')

def line5(request):
    return render(request, 'line3/line5.html')

def line6(request):
    return render(request, 'line3/line6.html')

def line7(request):
    return render(request, 'line3/line7.html')

def line8(request):
    return render(request, 'line3/line8.html')


@api_view(['POST'])
def train_data(request):
    if request.method == 'POST':
        serializer = TrainDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)