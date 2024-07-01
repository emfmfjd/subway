from django.shortcuts import render

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