# zelf gemaakt bestand
from django.urls import path
# from blog import views
from . import views

urlpatterns = [
    path('', views.home),
    path('post/<int:pk>/', views.post_detail, name='post_inhoud'),
    #path('blog/post_list.html', views.postlijst),
    path('blog/post_list.html', views.post_list, name='post_list'),

    path('JavaBlog/Javablog.html', views.javablog),
    path('JavaBlog/Blog5.html', views.Blog5gegevensbestand),
    path('JavaBlog/Blogdetail.html', views.Blogdetail),
     path('JavaBlog/BlogInvullen.html', views.BlogInvullen),

    path('', views.home),
    path('site/index.html/', views.home),
    path('site/overons.html/', views.ons),
    path('site/tarieven.html/', views.tarieven),
    path('site/contact.html/', views.contact),

    path('React/EenPagina.html/', views.PaginaReact),
]
