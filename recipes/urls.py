from django.urls import path, include
from recipes.views import my_view,home,contato


urlpatterns = [
    path('sobre/', my_view),
    path('contato/', contato),
    path('', home),
]