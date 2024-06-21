from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    return HttpResponse('teste')

def home(request):
    return render(request,'recipes/home.html', context={
                  'name':'lucas Garre'})

def contato(request):
    return render(request,'recipes/contato.html')

