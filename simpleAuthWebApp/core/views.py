from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.template import loader
from django.http import HttpResponse
from .forms import SignupForm
from .models import Post # Comment


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


# unused function
def home(request):
    template = loader.get_template('core/home.html')
    context = {'posts' : Post.objects.all()}
    return HttpResponse(template.render(context))


def explore(request):
    template = loader.get_template('core/explore.html')
    context = {'posts ': Post.objects.all()}
    return HttpResponse(template.render(context))
