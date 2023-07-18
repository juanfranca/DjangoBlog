from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostForm
from django.utils import timezone

def home(request):
    posts = Posts.objects.all().order_by('-published_date')
    form = PostForm
    return render(request, 'home.html', {'posts':posts, 'form':form})


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.author = request.user
            posts.published_date = timezone.now()
            posts.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create.html', {'form':form})

def edit(request, id):
    post = Posts.objects.get(id=id)
    form =PostForm(initial={'title': post.title, 'description':post.description})
    return render(request, 'edit.html', {'posts':post, 'form':form})

def update(request, id):
    posts = Posts.objects.get(id=id)
    if request.method =='POST':
        form = PostForm(request.POST, instance=posts)
        if form.is_valid():
            posts=form.save()
            posts.author = request.user
            posts.published_date = timezone.now()
            posts.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'home,html', {'form':form})

def delete(request, id):
    posts = Posts.objects.get(id=id)
    posts.delete()
    return redirect('home')


