from django.urls import path, re_path
import re

from . import views

urlpatterns = [
	path('substitutes_list/<int:product_id>/', views.search_substitutes, name='substitutes_list'),
    path('search/', views.search_product, name='search_product'),
    path('<int:product_id>/', views.description),
]
