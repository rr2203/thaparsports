from django.shortcuts import render
from .models import imagegallery

#from .models import Post


def home(request):
    gallery = imagegallery.objects.all()
    context = {
        "gallery": gallery,
    }
    return render(request, 'gallery2/index.html',context)