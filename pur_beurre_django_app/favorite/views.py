from django.shortcuts import render

from django.http import HttpResponse

def favorites_list(request):
    message = "Page de la liste des favoris favorites_list.html"
    return HttpResponse(message)