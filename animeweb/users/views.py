from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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