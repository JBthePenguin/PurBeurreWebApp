from django.urls import path, re_path
import re

from . import views

urlpatterns = [
	path('list/<int:product_id>/', views.products_list, name='products_list'),
    path('search/', views.search_substitute, name='search_substitute'),
    path('<int:product_id>/', views.description),
]
