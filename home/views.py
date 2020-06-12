
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from .forms import SignUpForm
# Create your views here.

class MyLoginView(LoginView):
    template_name = 'registration/login.html'

def log(request):
    return render(request,'registration/login.html')

def home(request):
    return render(request,'registration/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'home/signup.html', {'form': form})

