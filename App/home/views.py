from django.shortcuts import render, redirect
from .models import Topic , Artical
from .form import Tform, Aform
# Create your views here.


def about(request):

    return render(request, 'about.html')

def contect(request):

    return render(request, 'contect.html')





def home(request):

    return render(request, 'base/home.html')


def topic(request):
    topics = Topic.objects.all()

    context = {'topics' : topics }

    return render(request, 'base/topic.html' , context)


def artical(request, pk):

    articals = Artical.objects.get(id = pk)

    context = {'articals' :articals}

    return render(request ,'base/artical.html' , context)



def addTopic(request):
    form = Tform()
    if request.method == "POST":
        form= Tform(request.POST)
        if form.is_valid:
            form.save()
            return redirect('topic')
    context = {'form' : form}

    return render (request, "base/adtopic.html", context)

def addartical(request):
    form = Aform()
    if request.method == "POST":
        form= Aform(request.POST)
        if form.is_valid:
            form.save()
            return redirect('topic')
    context = {'form' : form}

    return render (request, "base/adtopic.html", context)