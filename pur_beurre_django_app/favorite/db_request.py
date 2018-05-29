#! /usr/bin/env python3
# coding: utf-8

from product.models import Product
from .example_mod import FAVORITES

def select_favorites(account_id):
    """ select all favorites for a specific account
    and return a list of them """
    # select all account's favorites in db
    all_favorites = FAVORITES
    account_favorites = []
    for favorite in all_favorites:
        if favorite["account_id"] == account_id:
            account_favorites.append(favorite)
    # construct favorite : {product: substitutes} -> [product, substitute]
    # construct favorites : [favorite]
    favorites = []
    for account_favorite in account_favorites:
        product = Product.objects.get(id=account_favorite["product_id"])
        substitute = Product.objects.get(id=account_favorite["substitute_id"])
        if len(favorites) == 0:
            # for the first favorite
            substitutes = []
            substitutes.append(substitute)
            favorites.append({product: substitutes})
        else:
            for favorite in favorites:
                try:
                    substitutes = favorite[product]
                except KeyError:
                    # create a new favorite with this product
                    substitutes = []
                    substitutes.append(substitute)
                    favorites.append({product: substitutes})
                    break
                else:
                    # add this substitute for the product -> update favorite
                    substitutes.append(substitute)
                    favorites.remove(favorite)
                    favorites.append({product: substitutes})
                    break
    # transform [{}] -> [[]]
    user_favorites = []
    for favorite in favorites:
        for product in favorite:
            substitutes = favorite[product]
            user_favorite = [product, substitutes]
            user_favorites.append(user_favorite)   
    return user_favorites
