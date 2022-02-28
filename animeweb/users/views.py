from django.shortcuts import get_object_or_404, render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from recommend.models import Anime
from users.models import UserList
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #hashed password
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} successfully created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def userList(request):
    return render(request, 'userlist.html')

def add_to_userlist(request, anime_id):
    new_anime = get_object_or_404(Anime, pk=anime_id)
    #if UserList.objects.filter(user=request.user, anime_in_list=anime_id).exists():
        #message fail
    user_list, created = UserList.objects.get_or_create(user=request.user)
    user_list.anime_in_list.add(new_anime)
    return render(request, "userlist.html")

class DeleteView(DeleteView):
    model = UserList
    field = UserList.anime_in_list
    context_object_name = 'anime-in-list'
    success_url = '/userlist'

@login_required
def profile(request):
    if request.method =='POST':
        updateForm = UserUpdateForm(request.POST, instance=request.user)
        profileForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if updateForm.is_valid and profileForm.is_valid():
            updateForm.save()
            profileForm.save()
            messages.success(request, f'Account successfully updated!')
            return redirect('profile')

    else:
        updateForm = UserUpdateForm(instance=request.user)
        profileForm = ProfileUpdateForm(instance=request.user.profile)

    context={
        'updateForm':updateForm,
        'profileForm':profileForm
    }

    return render(request, 'profile.html', context)