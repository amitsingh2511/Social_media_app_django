from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.to 
def index(request):
    return HttpResponse("wel come to social app")
