from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Images_info
from .imageAnalyzer import imagePredict

def home(request):
    return render(request, 'home.html')

def newimg(request):
    return render(request, 'newimg.html')


def result(request):
    image = Images_info()
    image.image_title = request.POST['title']
    image.image_data = request.FILES['images']
    image.image_pub_date = timezone.datetime.now()
    image.author = request.user
    image.save()
    label = imagePredict(image.image_data.url)
    return render(request, 'result.html', {'image' : image, 'label' : label})

def history(request):
    images = Images_info.objects.filter(author=request.user)
    return render(request, 'history.html', {'images' : images})