from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello (request):
    return HttpResponse("<H1>HELLO WORLD!!</H1>")
def about (request):
    return HttpResponse("<H1>ABOUT!!</H1>")
