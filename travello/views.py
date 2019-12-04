from django.shortcuts import render
from .models import destination
# Create your views here.
# Here we just made our homepage function 'home

def travello(request):

    dests = destination.objects.all()
    return render(request, 'travello.html', {'dests':dests})

def about(request):
    return render(request,'about.html')

def destinations(request):
    return render(request,'destinations.html')