from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Images_info
from .imageAnalyzer import imagePredict
import os
import mimetypes

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

def delete(request, image_id) :
    image = Images_info.objects.get(id=image_id)
    image.delete()
    return redirect('history')

def downloads(request, image_id) :
    image = Images_info.objects.get(id=image_id)
    image_url = image.image_data.url
    image_name = image_url[14:]
    image_type = mimetypes.guess_type(image_name)
    with open('.'+image_url, 'rb') as img :
        response = HttpResponse(img.read(), content_type=image_type[0])
        response["Content-Disposition"] = "attachment; filename" + os.path.basename(image_url)
        return response
    return redirect('history')