from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('product/index.html')
    return HttpResponse(template.render(request=request))

def products_list(request):
    message = "Page de résultat products_list.html"
    return HttpResponse(message)

def description(request):
    message = "Page descriptive d'un produit product.html"
    return HttpResponse(message)
