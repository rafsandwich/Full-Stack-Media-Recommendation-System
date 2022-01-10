from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# takes requests, returns response

def index(request):
    return render(request, 'index.html')

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
    