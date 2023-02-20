from django.shortcuts import render
from .models import Customer


def index(request):
    """ A view to return the index page"""
    return render(request, 'home/index.html')


""" Sign up Form """


def sign_up(request):
    if request.method == "POST":
        form = Customer(request.POST)
        if form.is_valid():
            form.save()
            return render(request, index.html)
    else:
        form = Customer()
        return render(request, 'signup.html', {'form': form})


def newsletter(request):
    """ A view to return the newsletter page"""
    template = 'home/newsletter.html'
    return render(request, template)
