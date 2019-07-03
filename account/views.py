from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm


def registration_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')

    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})