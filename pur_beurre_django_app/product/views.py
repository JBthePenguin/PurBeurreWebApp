#! /usr/bin/env python3
# coding: utf-8
from django.urls import reverse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from product.search_request import found_product, found_substitutes
from .models import Product

# VIEWS
def index(request, alert_message=False):
    context = {
        "alert_message": alert_message,
    }
    return render(request, 'product/index.html', context)


def search_substitutes(request, product_id):
    product, substitutes = found_substitutes(product_id)
    if substitutes.count() == 0:
        substitutes_pag = False
    else:
        paginator = Paginator(substitutes, 6)
        page = request.GET.get('page')
        try:
            substitutes_pag = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            substitutes_pag = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            substitutes_pag = paginator.page(paginator.num_pages)
    context = {
        "product": product,
        "substitutes" : substitutes_pag,
        "paginate": True
    }
    return render(request, 'product/substitutes_list.html', context)


def search_product(request):
    search_term = request.GET.get('search_term')
    product = found_product(search_term)
    if product in ["API connect error", "api no result", "db no result"]:
        return index(request, product)
    return redirect('substitutes_list', product.id)

def description(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product
    }
    return render(request, 'product/product.html', context)
