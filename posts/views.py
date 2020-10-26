from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.


def post(request):
    post_list = Post.objects.all().order_by('-id')

    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) | Q(content__icontains=query))

    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    post_list = paginator.get_page(page)
    context = {
        'posts': post_list
    }
    return render(request, "posts/posts.html", context)


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post
    }
    return render(request, "posts/detail.html", context)


@login_required(login_url='home')
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save()
            return redirect(reverse('detail', kwargs={'id': post.id}))
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, "posts/create.html", context)


def update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None,
                    request.FILES or None, instance=post)
    if form.is_valid():
        post.save()
        return redirect(reverse('detail', kwargs={'id': post.id}))
    context = {
        'form': form
    }
    return render(request, "posts/update.html", context)


def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse('post'))
