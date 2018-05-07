from django.shortcuts import render
from django.http import HttpResponse

def connect_create_account(request):
    message = "Page de connection et d'inscription connect_create_account.html"
    return HttpResponse(message)

def my_account(request):
    message = "Page descriptive du compte my_account.html"
    return HttpResponse(message)
