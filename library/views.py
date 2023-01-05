from django.shortcuts import render
from django.http import HttpResponse

# change for git

def home(request):
    return HttpResponse("LIBRARY PROJECT")