from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('blogHome', views.blogHome, name="blogHome"),
    path('postComment', views.postComment, name="postComment"),
    path('<str:slug>', views.blogPost, name="blogPost"),
   # path('blogPost', views.blogPost, name="blogPost"),

]
