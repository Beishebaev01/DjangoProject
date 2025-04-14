from django.shortcuts import render, HttpResponse
from posts.models import Post


def test_view(request):
    return HttpResponse("Hello, world!")


def html_view(request):
    return render(request, 'base.html')


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', context={'posts': posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/post_detail.html', context={'post': post})