from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    # return HttpResponse('HOME')
    return render(request, 'recipes/home.html')

def my_view(request):
    # return HttpResponse('SOBRE')
    return render(request, 'temp.html')

def contato(request):
    return HttpResponse('CONTATO')