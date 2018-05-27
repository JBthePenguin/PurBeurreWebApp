#! /usr/bin/env python3
# coding: utf-8

from django.shortcuts import render

from .models import Product


# VIEWS
def index(request):
    return render(request, 'product/index.html')

def products_list(request, prod_searched, substitutes):
    context = {
        "prod_searched": prod_searched,
        "substitutes" : substitutes
    }
    return render(request, 'product/products_list.html', context)

def search_substitute(request):
    prod_searched = Product.objects.get(id=1008)
    substitutes = [
        Product.objects.get(id=2058),
        Product.objects.get(id=2008),
        Product.objects.get(id=4058),
        Product.objects.get(id=2658),
        Product.objects.get(id=12500),
        Product.objects.get(id=10058),
    ]
    return products_list(request, prod_searched, substitutes)

def description(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product
    }
    return render(request, 'product/product.html', context)
