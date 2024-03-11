from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from . models import Post
from django.views.generic import ListView, DetailView


def post_list(request):
    posts = Post.objects.filter(date__lte=timezone.now()).order_by('date')
    # posts = Post.objects.all()
    return render(request, 'blog/post_list.html',{'posts': posts })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_inhoud.html', {'post':post})

# def postlijst(request):
#   return render(request, 'blog/post_list.html',{})

# Javascript blog
def javablog(request):
    return render(request, 'JavaBlog/Javablog.html',{})

def Blog5gegevensbestand(request):
    return render (request, 'JavaBlog/Blog5.html', {})

def Blogdetail(request):
    return render (request, 'JavaBlog/Blogdetail.html', {})

def BlogInvullen(request):
    return render (request, 'JavaBlog/BlogInvullen.html', {})

# site views

def home(request):
    return render (request, 'site/index.html', {})

def ons(request):
    return render (request, 'site/overons.html', {})

def tarieven(request):
    return render (request, 'site/tarieven.html', {})

def contact(request):
    return render (request, 'site/contact.html', {})


# react

def PaginaReact(request):
 return render(request, 'React/Eenpagina.html', {})
