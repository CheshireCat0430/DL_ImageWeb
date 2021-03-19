from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('newimg/', views.newimg, name='newimg'),
    path('result/', views.result, name='result'),
    path('history/', views.history, name='history'),
    path('downloads/<int:image_id>/', views.downloads, name='downloads'),
    path('delete/<int:image_id>/', views.delete, name='delete'),
]