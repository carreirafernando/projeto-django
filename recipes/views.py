from django.shortcuts import render


# Create your views here.
def home(request):
    # return HttpResponse('HOME')
    return render(request, 'recipes/home.html'),
