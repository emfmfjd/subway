from django.urls import path

from . import views

app_name = 'subway'

urlpatterns = [
    path('3호선/', views.line3, name='3호선')
]