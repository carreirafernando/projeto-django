from django.urls import path

from recipes.views import contato, home, my_view

urlpatterns = [
    path('', home),
    path('sobre/', my_view),
    path('contato/', contato),
]