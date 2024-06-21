from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    return HttpResponse('teste')

def home(request):
    return render(request,'recipes/home.html')

def contato(request):
    return HttpResponse('Contato')

