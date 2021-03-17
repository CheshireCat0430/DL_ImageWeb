from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('newimg/', views.newimg, name='newimg'),
    path('result/', views.result, name='result'),
    path('history/', views.history, name='history'),
]