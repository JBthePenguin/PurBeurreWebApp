#! /usr/bin/env python3
# coding: utf-8

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .db_request import select_favorites 


class Favorite:
    def __init__(self, product, substitutes):
        self.product = product
        self.substitutes = substitutes


@login_required
def favorites_list(request):
    user_favorites = select_favorites(request.user.id)
    context = {
        "favorites": user_favorites,
    }
    return render(request, 'favorite/favorites.html', context)
