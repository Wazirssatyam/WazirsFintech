from django.shortcuts import render,redirect,HttpResponse
from block.models import slider, team
# Create your views here.
def index(request):
    slide=slider.objects.all()
   
    return render(request,'index.html',{'image':slide})
def teams(request):
    teams=team.objects.all()
    return render(request,'team.html',{'data':teams})

