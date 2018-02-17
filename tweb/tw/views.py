from django.shortcuts import render

# Create your views here.
from .models import Post


def home(request):
    post = Post.objects.all().order_by('-timestamp')
    context = {
        "post": post,
    }
    return render(request, 'tw/index.html', context)



def eventlist(request):
    post = Post.objects.all().order_by('-timestamp')
    context = {
        "post": post,
    }
    return render(request, 'tw/eventlist.html', context)

def r_eventlist(request):
    post = Post.objects.all().order_by('-timestamp')
    context = {
        "post": post,
    }
    return render(request, 'tw/r_eventlist.html', context)

def achieve(request):
    post = Post.objects.all().order_by('-timestamp')
    context = {
        "post": post,
    }
    return render(request, 'tw/achieve.html', context)

# def detail(request):
#     post = Post.objects.all().order_by('-timestamp')
#     context = {
#         "post": post,
#     }
#     return render(request, 'tw/detail.html', context)

def detail(request, Post_id):
    try:
        post= Post.objects.get(pk=Post_id)
    except Post.DoesNotExist:
        raise Http404("Post Does Not Exist")
    return render(request,'tw/detail.html',{'post':post})
