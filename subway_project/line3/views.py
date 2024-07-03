from django.shortcuts import render

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

