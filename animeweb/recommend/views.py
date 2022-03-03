from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView
from .models import Anime, Tag
from users.models import UserList
from .forms import MessageForm

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
    return render(request, 'index.html', {'form': MessageForm()})

def recResults(request):
    if request.method=='POST':
        artstyles= request.POST["artstyles"]
        lengthAnime= request.POST["length-anime"]
        prodStatus = request.POST["prod-status"] 
        genres = request.POST.getlist("genres")

        styleYear = 2012
        animes = Anime.objects.all()
        recommendedAnimes = []

        if int(artstyles) > styleYear:
            for anime in animes:
                if int(lengthAnime) == 1:
                    if anime.episodes == 1 and anime.year > styleYear:
                        if genres:
                            for genre in genres:
                                for t in anime.tags.all():
                                    if t.tag == genre:
                                        if anime not in recommendedAnimes:     #wanted to use a set, wouldn't pass
                                            if prodStatus == "ONGOING":                                    
                                                recommendedAnimes.append(anime)
                                            else:
                                                if anime.status == "FINISHED":
                                                    recommendedAnimes.append(anime)
                        else:
                            if prodStatus == "ONGOING":                                    
                                recommendedAnimes.append(anime)
                            else:
                                if anime.status == "FINISHED":
                                    recommendedAnimes.append(anime)
                elif int(lengthAnime) > 12:
                    if anime.episodes > 12 and anime.year > styleYear:
                        if genres:
                            for genre in genres:
                                for t in anime.tags.all():
                                    if t.tag == genre:
                                        if anime not in recommendedAnimes:                                        
                                            if prodStatus == "ONGOING":                                    
                                                recommendedAnimes.append(anime)
                                            else:
                                                if anime.status == "FINISHED":
                                                    recommendedAnimes.append(anime)
                        else:
                            if prodStatus == "ONGOING":                                    
                                recommendedAnimes.append(anime)
                            else:
                                if anime.status == "FINISHED":
                                    recommendedAnimes.append(anime)
                else:
                    if anime.episodes <= 12 and anime.episodes > 1 and anime.year > styleYear:
                        if genres:
                            for genre in genres:
                                for t in anime.tags.all():
                                    if t.tag == genre:
                                        if anime not in recommendedAnimes:                                        
                                            if prodStatus == "ONGOING":                                    
                                                recommendedAnimes.append(anime)
                                            else:
                                                if anime.status == "FINISHED":
                                                    recommendedAnimes.append(anime)
                        else:
                            if prodStatus == "ONGOING":                                    
                                recommendedAnimes.append(anime)
                            else:
                                if anime.status == "FINISHED":
                                    recommendedAnimes.append(anime)
        else:
            for anime in animes:
                if int(lengthAnime) == 1:
                    if anime.episodes == 1 and anime.year <= styleYear:
                        if genres:
                            for genre in genres:
                                for t in anime.tags.all():
                                    if t.tag == genre:
                                        if anime not in recommendedAnimes:                                        
                                            if prodStatus == "ONGOING":                                    
                                                recommendedAnimes.append(anime)
                                            else:
                                                if anime.status == "FINISHED":
                                                    recommendedAnimes.append(anime)
                        else:
                            if prodStatus == "ONGOING":                                    
                                recommendedAnimes.append(anime)
                            else:
                                if anime.status == "FINISHED":
                                    recommendedAnimes.append(anime)
                elif int(lengthAnime) > 12:
                    if anime.episodes > 12 and anime.year <= styleYear:
                        if genres:
                            for genre in genres:
                                for t in anime.tags.all():
                                    if t.tag == genre:
                                        if anime not in recommendedAnimes:                                        
                                            if prodStatus == "ONGOING":                                    
                                                recommendedAnimes.append(anime)
                                            else:
                                                if anime.status == "FINISHED":
                                                    recommendedAnimes.append(anime)
                        else:
                            if prodStatus == "ONGOING":                                    
                                recommendedAnimes.append(anime)
                            else:
                                if anime.status == "FINISHED":
                                    recommendedAnimes.append(anime)
                else:
                    if anime.episodes <= 12 and anime.episodes > 1 and anime.year <= styleYear:
                        if genres:
                            for genre in genres:
                                for t in anime.tags.all():
                                    if t.tag == genre:
                                        if anime not in recommendedAnimes:                                        
                                            if prodStatus == "ONGOING":                                    
                                                recommendedAnimes.append(anime)
                                            else:
                                                if anime.status == "FINISHED":
                                                    recommendedAnimes.append(anime)
                        else:
                            if prodStatus == "ONGOING":                                    
                                recommendedAnimes.append(anime)
                            else:
                                if anime.status == "FINISHED":
                                    recommendedAnimes.append(anime)                


        context = {
            'artstyles': artstyles,
            'length_anime':lengthAnime,
            'genres': genres,
            #'animes': Anime.objects.all()
            'animes':recommendedAnimes
        }
        return render(request, 'recommend-results.html', context)

    return render(request, 'recommend-results.html')

class AnimeListView(ListView):
    model = Anime
    template_name = 'all-anime.html' #<model> name _ <viewtype>
    context_object_name = 'animes'
    ordering = ['title'] #ordering most recent anime first (year)?
    paginate_by = 9

    # def get_context_data(self, **kwargs):
    #     context=  super().get_context_data(**kwargs)
    #     search_input = self.request.GET.get('search-area') or ''
    #     if search_input:
    #         context['animes'] = context['animes'].filter(title__icontains=search_input)

    #     context['search_input'] = search_input
    #     return context


    # IGNORE    <form method = "GET">
    #    <input type ="text" name='search-area' value="{{ search_input }}">
    #    <input type="submit" value='Search'>
    #</form>
    # <form method = "GET" action='/anime_search/'>
    #     <input type ="text" name='q' placeholder="search">
    # </form>

class AnimeDetailView(DetailView):
    model = Anime
    template_name = 'anime_details.html'

# def anime_search(request):
#     query = request.GET.get("q", None)
#     qs = Anime.objects.all()
#     if query is not None:
#         qs = qs.filter(title__icontains=query)
#     context = {
#         "object_list": qs,
#     }
#     return render(request, "all-anime.html", context)

@login_required
def all_anime(request):
    if request.method == 'POST':
        addToList = request.POST.get('listAdd')
        if addToList:
            new_anime = get_object_or_404(Anime, pk=addToList)
            user_list, created = UserList.objects.get_or_create(user=request.user)
            user_list.anime_in_list.add(new_anime)
            messages.success(request, f'Anime successfully added to your List!')
            template = loader.get_template('all-anime.html')
            context = {
                'animes': Anime.objects.all(),
                'messages':messages
            }
            return HttpResponse(template.render(context, request))
        
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
    