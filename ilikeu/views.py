from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.utils.datetime_safe import datetime

from .forms import PostForm, LoginForm
from .models import Human
from django.http import response
from django.shortcuts import get_object_or_404, redirect, render

from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'blog/login.html', {})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data.get('gender')
            mate_date = form.cleaned_data.get('mate_date')
            mateDate = datetime.date(mate_date).strftime("%Y-%m-%d")
            phone_number = form.cleaned_data.get('phone_number')
            password = form.cleaned_data.get('password')
            Human.objects.filter(phoneNumber=phone_number)
            actor = 1
            if actor:
                return render(request, 'blog/profile-page.html', {})
            else:
                return render(request, 'blog/login.html', {})
    else:
        return HttpResponse("Nothing happend")
    # return render(request, 'blog/profile-page.html', {})

def vote(request, mate_date, number):
    return render(request, 'blog/profile-page.html', {})

def result(request, mate_date, number):
    return HttpResponse("Here's result Page")

# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form' : form})
#
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form':form})
#
# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html',{'posts': posts})
#
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post':post})
