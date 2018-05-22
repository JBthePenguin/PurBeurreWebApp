#! /usr/bin/env python3
# coding: utf-8

from django.shortcuts import render

from .models import PRODUCTS

# VIEWS
def index(request):
    return render(request, 'product/index.html')

def products_list(request, products):
    prod_searched = products[0]
    substitutes = products[1:]
    context = {
        "prod_searched": prod_searched,
        "substitutes" : substitutes
    }
    return render(request, 'product/products_list.html', context)

def search_substitute(request):
    return products_list(request, PRODUCTS)

def description(request, product_id):
    prod_id = int(product_id)
    for product in PRODUCTS:
        if product["id"] == prod_id:
            prod_selected = product
    context = {
        "product": prod_selected
    }
    return render(request, 'product/product.html', context)
