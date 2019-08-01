from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post, Author
from .forms import PostModelForm
# Create your views here.


def redirect_view(request):
    return redirect('posts')


def post_list(request):
    all_posts = Post.objects.all()
    messages.info(request, 'here are all posts')
    return render(request, 'posts/posts_list.html', context={'posts': all_posts})


def post_details(request, slug):
    unique_post = get_object_or_404(Post, slug=slug)
    context = {
        'post': unique_post
    }
    messages.info(request, 'here are details')

    return render(request, 'posts/post_details.html', context)


def post_create(request):
    author, created = Author.objects.get_or_create(
        user=request.user, email=request.user.email, cellphone_num='01521408723')
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print('hello', form.is_valid())
        form.instance.author = author
        form.save()
        return redirect('posts')
    context = {
        'form': form
    }
    messages.info(request, 'created')

    return render(request, 'posts/post_create.html', context)


def post_update(request, slug):
    unique_post = get_object_or_404(Post, slug=slug)
    form = PostModelForm(request.POST or None,
                         request.FILES or None, instance=unique_post)
    print('valid', form.is_valid())
    if form.is_valid():
        form.save()
        return redirect('posts')
    context = {
        'form': form
    }
    messages.info(request, 'Edited')
    return render(request, 'posts/post_update.html', context)


def post_delete(request, slug):
    unique_post = get_object_or_404(Post, slug=slug)
    unique_post.delete()
    messages.info(request, 'deleted')

    return redirect('posts')
