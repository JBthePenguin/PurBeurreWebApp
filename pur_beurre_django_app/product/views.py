#! /usr/bin/env python3
# coding: utf-8

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django import forms

from .models import PRODUCTS


# VIEWS
def index(request):
    template = loader.get_template('product/index.html')
    return HttpResponse(template.render(request=request))

def products_list(request, products):
    prod_searched = products[0]
    substitutes = products[1:]
    context = {
        "prod_searched": prod_searched,
        "substitutes" : substitutes
    }
    template = loader.get_template('product/products_list.html')
    return HttpResponse(template.render(context))

def search_substitute(request):
    return products_list(request, PRODUCTS)

def description(request, product_id):
    prod_id = int(product_id)
    for product in PRODUCTS:
        if product["id"] == prod_id:
            prod_selected = product
    message = "Page descriptive de " + prod_selected["name"] + "  marque: " + prod_selected["brands"] + "  ---> product.html"
    return HttpResponse(message)
