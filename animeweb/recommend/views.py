from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# takes requests, returns response

animeDummy = [
    {
        'title':'Hunter x Hunter',
        'type':'TV',
        'episodes':'62',
        'year':'2013',
        'production_status': 'ongoing',
        'picture':'https://cdn.myanimelist.net/images/anime/8/19473.jpg',
    },
    {
        'title':'Dragon ball',
        'year':'1990',
        'production_status': 'finished',
        'picture':'https://cdn.myanimelist.net/images/anime/1887/92364.jpg',
    },
]


def index(request):
    context = {
        'animes': animeDummy 
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html', {'title':'About'})

def say_hello(request):
    #pull data from db, transform data, send emails

    context = {
        'name' : 'Sachi',
        'over18' : True,
        'favourite' : 'action',
    }
    return render(request, 'hello.html', context)
    