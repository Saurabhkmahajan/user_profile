from audioop import reverse
from pyexpat.errors import messages

from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.http import HttpResponseRedirect

from . import forms, models
from .models import Profile
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm

# Create your views here.


def show_profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles.html', {'profiles': profiles})


def single_profile(request):
    single_profile = Profile.objects.all()
    return render(request, 'single_profile.html',{'profile': single_profile})


def add_profile(request):
     if request.method == 'POST':
      form = ProfileForm(request.POST,request.FILES)
     if form.is_valid():
      profile = form.save(commit=False)
     profile.save()
     return redirect('show_profiles') 
     form = ProfileForm()
     return render(request, 'add_profile.html',
    {'form': form})

def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            return HttpResponseRedirect(reverse('home'))  # TODO: go to profile
    return render(request, 'accounts/sign_up.html', {'form': form})

def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(
                        reverse('home')  # TODO: go to profile
                    )
                else:
                    messages.error(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.error(
                    request,
                    "Username or password is incorrect."
                )
    return render(request, 'accounts/sign_in.html', {'form': form})

 
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect(reverse('accounts:profile'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

def edit_profile(request):
    user = request.user0
    profile = get_object_or_404(models.Profile, user=user)
    form = forms.ProfileForm(instance=profile)

    if request.method == 'POST':
        form = forms.ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated the Profile Successfully!")
            return HttpResponseRedirect(reverse('accounts:profile'))

    return render(request, 'accounts/edit_profile.html', {
        'form': form
    })

