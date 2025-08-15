from django.shortcuts import render,redirect,get_object_or_404
from .models import PostModel
# Create your views here.


def index(request):
    return render(request, 'blog/index.html', {})


def post(request,slug):
    post=get_object_or_404(PostModel,slug=slug)
    return render(request, 'blog/post.html', {'post':post})


def posts(request):
    all_posts=PostModel.objects.all()
    return render(request, 'blog/posts.html', {'all_posts':all_posts})
