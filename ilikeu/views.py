from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from .forms import PostForm
from .models import Post
from .models import Man
from .models import Woman

# ---------------------------------

from django.http import HttpResponse

# Create your views here.

def home(request):
    form = PostForm()
    return render(request, 'blog/login.html', {'form': form})

def login(request):
    return render(request, 'blog/profile-page.html', {})

def logout(request):
    # return render(request, 'blog/logout.html',{})
    logout(request)
    return HttpResponseRedirect('/')

def vote(request, mate_date, number):
    return render(request, 'blog/profile-page.html', {})

def result(request, mate_date, number):
    return HttpResponse("Here's result Page")

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form' : form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})