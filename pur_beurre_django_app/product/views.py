from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    message = "Page d'accueil search_product.html"
    return HttpResponse(message)

def products_list(request):
    message = "Page de résultat products_list.html"
    return HttpResponse(message)

def description(request):
    message = "Page descriptive d'un produit product.html"
    return HttpResponse(message)
