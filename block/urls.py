
from django.urls import path,include
from block import views
urlpatterns = [
    path("",views.index,name='index'),
    path("team/",views.teams,name='teams'),
    path("about/",views.about,name='about'),
    path("blogs/",views.blogs,name='blogss'),
    path("blogss/<int:pk>",views.blogssingle,name='blogspage')
]
