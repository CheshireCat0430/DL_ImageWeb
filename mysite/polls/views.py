from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Images
from .imageAnalyzer import imagePredict

def home(request):
    return render(request, 'home.html')

def newimg(request):
    return render(request, 'newimg.html')


def result(request):
    images = Images()
    images.title = request.POST['title']
    images.imageInfo = request.FILES['images']
    images.pub_date = timezone.datetime.now()
    images.save()
    label = imagePredict(images.imageInfo.url)
    return render(request, 'result.html', {'images' : images, 'label' : label})