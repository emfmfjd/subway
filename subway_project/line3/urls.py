# line3/urls.py
from django.urls import path
from . import views

app_name = 'line3'

urlpatterns = [
    path('', views.index, name='index'),
    path('1호선/', views.line1, name='1호선'),
    path('2호선/', views.line2, name='2호선'),
    path('3호선/', views.line3, name='3호선'),
    path('4호선/', views.line4, name='4호선'),
    path('5호선/', views.line5, name='5호선'),
    path('6호선/', views.line6, name='6호선'),
    path('7호선/', views.line7, name='7호선'),
    path('8호선/', views.line8, name='8호선'),
]