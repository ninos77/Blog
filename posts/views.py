from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def post(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "posts/posts.html", context)


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post
    }
    return render(request, "posts/detail.html", context)
