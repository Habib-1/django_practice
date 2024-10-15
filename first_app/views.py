from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hired(request):
    return HttpResponse("Please hire me")
def hire_team(request):
    return HttpResponse("You Have To Pay 100$")