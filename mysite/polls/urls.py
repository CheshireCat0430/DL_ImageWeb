from django.urls import path
from . import views

urlpatterns = [
    path('newimg/', views.newimg, name='newimg'),
    path('result/', views.result, name='result'),
]