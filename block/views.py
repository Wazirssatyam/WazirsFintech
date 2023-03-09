from django.shortcuts import render,redirect,HttpResponse
from block.models import slider, team ,blog
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    slide=slider.objects.all()
   
    return render(request,'index.html',{'image':slide})
def teams(request):
    teams=team.objects.all()
    return render(request,'team.html',{'data':teams})

def about(request):
    teams=team.objects.all()
    return render(request,'about.html',{'data':about})
def blogs(request):
    posts = blog.objects.all()
    
    p = Paginator(posts, 1) 
    
    page_number = request.GET.get('page')
    try:
        print(1)
        page_obj = p.get_page(page_number) 
        print(page_obj) 
    except PageNotAnInteger:
        print(2)
        page_obj = p.page(1)
    except EmptyPage:
        print(3)
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
   
    return render(request, 'blog.html', context)
def blogssingle(request,pk):
    data = blog.objects.filter(id=pk)
    print(data)
    return render(request, 'blogsingle.html',{'data':data})
