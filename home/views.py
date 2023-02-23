from django.shortcuts import render
from .models import Customer


def index(request):
    # A view to return the index page
    return render(request, 'home/index.html')


# Sign up Form


def sign_up(request):
    if request.method == "POST":
        form = Customer(request.POST)
        if form.is_valid():
            form.save()
            return render(request, index.html)
    else:
        form = Customer()
        return render(request, 'signup.html', {'form': form})


def privacy_policy(request):
    # A view to render the privacy policy page

    return render(request, 'home/privacy_policy.html')


def terms_and_conditions(request):
    # A view to render the terms and conditions page

    return render(request, 'home/terms_and_conditions.html')


def return_and_refund_policy(request):
    # A view to render the return and refund policy page

    return render(request, 'home/return_and_refund_policy.html')


def newsletter(request):
    # A view to return the newsletter page
    template = 'home/newsletter.html'
    return render(request, template)
