#! /usr/bin/env python3
# coding: utf-8

from .models import Product


def save_product(product_api):
    """ save a product from API in DB """
    # check if the product is in DB
    try:
        product = Product.objects.get(code=product_api["code"])
    except Product.DoesNotExist:
        # save product in DB
        try:
            brands = product_api["brands"]
        except KeyError:
            brands = ""
        try:
            image_url = product_api["image_url"]
        except KeyError:
            image_url = ""
        try:
            image_small_url = product_api["image_url"]
        except KeyError:
            image_small_url = ""
        try:
            nutrient_level = product_api["nutrient_levels"]
            fat = nutrient_level["fat"]
            salt = nutrient_level["salt"]
            sugars = nutrient_level["sugars"]
            saturated_fat = nutrient_level["saturated-fat"]
        except KeyError:
            fat = ""
            salt = ""
            sugars = ""
            saturated_fat = ""
        try:
            nutriments = product_api["nutriments"]
            fat_100g = nutriments["fat"]
            salt_100g = nutriments["salt"]
            saturated_fat_100g = nutriments["saturated-fat_100g"]
            sugars_100g = nutriments["sugars_100g"]
        except KeyError:
            fat_100g = ""
            salt_100g = ""
            saturated_fat_100g = ""
            sugars_100g = ""
        product = Product(
            code=product_api["code"],
            product_name=product_api["product_name"],
            categories=product_api["categories"],
            brands=brands,
            nutrition_grades=product_api["nutrition_grades"],
            url=product_api["url"],
            image_url=image_url,
            image_small_url=image_small_url,
            fat=fat,
            salt=salt,
            saturated_fat=saturated_fat,
            sugars=sugars,
            fat_100g=fat_100g,
            saturated_fat_100g=saturated_fat_100g,
            sugars_100g=sugars_100g,
            salt_100g=salt_100g,)
        product.save()
