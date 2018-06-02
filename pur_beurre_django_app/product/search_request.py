#! /usr/bin/env python3
# coding: utf-8

import openfoodfacts
from requests.exceptions import ConnectionError
from .models import Product


def found_product(search_term):
    """ make request to API openfoodfacts to found a product
    get it in db and return it """
    #API request
    try:
        search_result = openfoodfacts.products.search(
            search_term, locale="fr"
        )
    except ConnectionError:
        product = "API connect error"
    else:
        products = search_result['products']
        try:
            product_api = products[0]
        except IndexError:
            # check if there is a result ...
            product = "api no result"
        else:
            new_request_in_db = True
            i = 0
            while new_request_in_db is True:
                # check if product is in db
                try:
                    product_api["code"]
                except KeyError:
                    i += 1
                    try:
                        product_api = products[i]
                    except IndexError:
                        product = "db no result"
                        new_request_in_db = False
                else:
                    try:
                        product = Product.objects.get(code=product_api["code"])
                    except Product.DoesNotExist:
                        i += 1
                        try:
                            product_api = products[i]
                        except IndexError:
                            product = "db no result"
                            new_request_in_db = False
                    else:
                        # check if it have categories
                        if product.categories == "":
                            i += 1
                            try:
                                product_api = products[i]
                            except IndexError:
                                product = "db no result"
                                new_request_in_db = False
                        else:
                            new_request_in_db = False
    return product


def found_substitutes(product_id):
    """ found substitutes for the product in db """
    # select products in the same categories with better or same grade
    product = Product.objects.get(id=product_id)
    list_categories = product.categories.split(",")
    list_categories = list_categories[-3:]
    categories = ",".join(list_categories)
    if categories[0] == " ":
        categories = categories[1:]
    # query select
    substitutes = Product.objects.filter(categories__contains=categories
        ).exclude(product_name=product.product_name, brands=product.brands
        ).filter(nutrition_grades__lte=product.nutrition_grades
        ).order_by("nutrition_grades", "product_name", "brands"
        ).distinct("nutrition_grades", "product_name"
    )
    return product, substitutes
