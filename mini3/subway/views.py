from django.shortcuts import render
from .models import TrainData
# Create your views here.

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

def train_mark(request):
    trains = TrainData.objects.all()
    context = {'train': trains}
    return render(request, 'subway/line3.html', context)

def train_marker_view(request):
    # 상행 기차와 하행 기차를 저장할 리스트 초기화
    up_trains = []
    down_trains = []

    # TrainData 모델에서 데이터 가져오기
    train_data = TrainData.objects.all()

    # 상행과 하행 기차 개수 세기
    for train in train_data:
        if train.updnLine.split()[0] == '상행':
            up_trains.append("상행_" + train)
        elif train.updnLine.split()[0] == '하행':
            down_trains.append("하행_" + train)

    # # 상행 기차 개수와 하행 기차 개수 출력 (테스트용)
    # print(f"상행 기차 개수: {len(up_trains)}")
    # print(f"하행 기차 개수: {len(down_trains)}")

    context = {
        'up_trains': up_trains,
        'down_trains': down_trains,
    }

    return render(request, 'subway/line3.html', context)

