from django.shortcuts import render
from .models import Post 

# Create your views here.
                                  

def index(request):
    if request.POST:
        title= request.POST["title"]
        body= request.POST["body"]
        instance = Post(title=title, body=body)
        instance.save()
    
    return render( request , 'index.html',{"posts" : Post.objects.all()} )



def post(request,pk):
    post = Post.objects.get(id=pk)
    return render(request,"post.html",{'post':post} )


def new(request):
    return render(request,"new.html" )


def submit(request):
    title= request.POST("title")
    body= request.POST("body")
    return render(request,"index.html" ,{"title":title , "body" : body}    )