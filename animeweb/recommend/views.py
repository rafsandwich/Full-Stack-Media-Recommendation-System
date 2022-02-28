from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView
from .models import Anime, Tag
from users.models import UserList

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
    return render(request, 'index.html')

class AnimeListView(ListView):
    model = Anime
    template_name = 'all-anime.html' #<model> name _ <viewtype>
    context_object_name = 'animes'
    #ordering = ['-year'] #ordering most recent anime first?
    paginate_by = 9

    def all_anime(request):
        if request.method == 'POST':
            addToList = request.POST.get('listAdd')
            if addToList:
                new_anime = get_object_or_404(Anime, pk=addToList)
                user_list, created = UserList.objects.get_or_create(user=request.user)
                user_list.anime_in_list.add(new_anime)
            
        else:
            template = loader.get_template('all-anime.html')
            context = {
                'animes': Anime.objects.all() 
            }
            return HttpResponse(template.render(context, request))

class AnimeDetailView(DetailView):
    model = Anime
    template_name = 'anime_details.html'

# def add_to_userlist(request, anime_id):
#     new_anime = get_object_or_404(Anime, pk=anime_id)
#     #if UserList.objects.filter(user=request.user, anime_in_list=anime_id).exists():
#         #message fail
#     user_list, created = UserList.objects.get_or_create(user=request.user)
#     user_list.anime_in_list.add(new_anime)
#     return render(request, "userlist.html")

def all_anime(request):
    if request.method == 'POST':
        addToList = request.POST.get('listAdd')
        if addToList:
            new_anime = get_object_or_404(Anime, pk=addToList)
            user_list, created = UserList.objects.get_or_create(user=request.user)
            user_list.anime_in_list.add(new_anime)
        
    else:
        template = loader.get_template('all-anime.html')
        context = {
            'animes': Anime.objects.all() 
        }
        return HttpResponse(template.render(context, request))
        #return render(request, 'all-anime.html', context)

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
    