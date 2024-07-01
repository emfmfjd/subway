from django.shortcuts import render

# Create your views here.

def line3(request):
    return render(request,'subway/line3.html')