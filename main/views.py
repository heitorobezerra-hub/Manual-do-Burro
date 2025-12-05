from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'site/home.html')

@login_required
def vestibular(request):
    return render(request, 'site/vestibular.html')


