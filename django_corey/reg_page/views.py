from django.shortcuts import render , redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created successfully! You are now able to log in')
            form.save()
            return redirect('login')

    else:
        form = UserRegisterForm()
    
    return render(request , 'register.html' , {'forms':form})


@login_required
def profile(request):
    return render(request , 'profile.html')