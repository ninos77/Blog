from django.shortcuts import render
from .models import Post

# Create your views here.

def post(request):
  context = {
    'posts' : Post.objects.all()
  }
  return render(request, "posts/posts.html",context)