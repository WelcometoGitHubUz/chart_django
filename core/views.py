from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'index.html', context)

def example(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }

    return render(request, 'example.html', context)

def doughnot(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }

    return render(request, 'details/doughnot.html',context)
def linechart(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }

    return render(request, 'details/linechart.html',context)
