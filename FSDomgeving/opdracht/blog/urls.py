# zelf gemaakt bestand
from django.urls import path
# from blog import views
from . import views

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_inhoud'),
    path('blog/post_list.html', views.postlijst),

    path('', views.home),
    path('site/index.html/', views.home),
    path('site/overons.html/', views.ons),
    path('site/tarieven.html/', views.tarieven),
    path('site/contact.html/', views.contact),
]
