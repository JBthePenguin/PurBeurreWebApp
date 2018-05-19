#! /usr/bin/env python3
# coding: utf-8

from django.shortcuts import render

from .models import PRODUCTS

def check_log_session(request):
    member = False
    if request.user.is_authenticated:
        member = True
    return member

# VIEWS
def index(request):
    member = check_log_session(request)
    context = {
        "member": member
    }
    return render(request, 'product/index.html', context)

def products_list(request, products):
    member = check_log_session(request)
    prod_searched = products[0]
    substitutes = products[1:]
    context = {
        "member": member,
        "prod_searched": prod_searched,
        "substitutes" : substitutes
    }
    return render(request, 'product/products_list.html', context)

def search_substitute(request):
    return products_list(request, PRODUCTS)

def description(request, product_id):
    member = check_log_session(request)
    prod_id = int(product_id)
    for product in PRODUCTS:
        if product["id"] == prod_id:
            prod_selected = product
    context = {
        "member": member,
        "product": prod_selected
    }
    return render(request, 'product/product.html', context)
