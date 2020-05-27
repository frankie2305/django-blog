from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def signup(req):
    if req.method == 'POST':
        form = UserSignupForm(req.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'Account has been successfully created for { username }!')
            return redirect('users:login')
    
    else:
        form = UserSignupForm()
    
    return render(req, 'users/signup.html', { 'title': 'Sign up', 'legend': 'Sign up', 'form': form, 'submit': 'Sign up', 'choice': 'Log in' })

@login_required
def profile(req):
    if req.method == 'POST':
        user_update_form = UserUpdateForm(req.POST, instance=req.user)
        profile_update_form = ProfileUpdateForm(req.POST, req.FILES, instance=req.user.profile)
        
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(req, f"{req.user.username}'s account has been successfully updated!")
            return redirect('users:profile')
    
    else:
        user_update_form = UserUpdateForm(instance=req.user)
        profile_update_form = ProfileUpdateForm(instance=req.user.profile)
    
    return render(req, 'users/profile.html', { 'title': f"{req.user.username}'s profile", 'legend': 'Update profile', 'choice': 'Change password', 'user_update_form': user_update_form, 'profile_update_form': profile_update_form, 'submit': 'Update' })
