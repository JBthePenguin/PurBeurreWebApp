#! /usr/bin/env python3
# coding: utf-8

from django.shortcuts import render, redirect

from product.search_request import found_product, found_substitutes

from .models import Product


# VIEWS
def index(request, alert_message=False):
    context = {
        "alert_message": alert_message,
    }
    return render(request, 'product/index.html', context)


def products_list(request, product, substitutes):
    context = {
        "product": product,
        "substitutes" : substitutes
    }
    return render(request, 'product/products_list.html', context)


def search_substitute(request):
    search_term = request.GET.get('search_term')
    product = found_product(search_term)
    if product in ["API connect error", "api no result", "db no result"]:
        return index(request, product)
    substitutes = found_substitutes(product)
    return products_list(request, product, substitutes)


def description(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product
    }
    return render(request, 'product/product.html', context)
