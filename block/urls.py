
from django.urls import path,include
from block import views
urlpatterns = [
    path("",views.index,name='index'),
    path("team/",views.teams,name='teams'),
]