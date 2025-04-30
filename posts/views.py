from django.shortcuts import render, HttpResponse, redirect
from posts.models import Post
from posts.forms import PostForm
from django.contrib.auth.decorators import login_required


def test_view(request):
    return HttpResponse("Hello, world!")


def html_view(request):
    return render(request, 'base.html')


@login_required(login_url='/login/')
def post_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'posts/post_list.html', context={'posts': posts})


@login_required(login_url='/login/')
def post_detail_view(request, post_id):
    
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return render(request, 'posts/post_detail.html', context={'post': post})


@login_required(login_url='/login/')
def post_create_view(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'posts/post_create.html', context={'form': form})
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            tags = form.cleaned_data.pop("tags")
            post = Post.objects.create(**form.cleaned_data)
            post.tags.set(tags)
            return redirect("/posts/")
        else:
            return render(request, 'posts/post_create.html', context={'form': form})
        

    