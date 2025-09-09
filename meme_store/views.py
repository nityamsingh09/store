from django.shortcuts import render,redirect,get_object_or_404
from .models import Meme,Giphy
# Create your views here.

def home(request):
    photos = Meme.objects.all()
    return render(request,'home.html',{'photos': photos})

def about(request):
    return render(request,"about.html")
    
    
def gippy(request):
    gipp = Giphy.objects.all()
    return render(request,'gippy.html',{'gipp':gipp})


def trending_meme(request):
    photos = Meme.objects.all().order_by('-likes') 
    return render(request,'trending.html',{'photos': photos})

def like_meme(request,meme_id):
    meme =get_object_or_404(Meme,id=meme_id)
    meme.likes +=1
    meme.save()
    return redirect('home')

def search(request):
    query = request.GET.get('q')
    memes = []
    giphys = []
    
    if query:
        memes = Meme.objects.filter(title__icontains=query)
        giphys = Giphy.objects.filter(title__icontains=query)

    return render(request, "search.html", {
        "query": query,
        "memes": memes,
        "giphys": giphys
    })

