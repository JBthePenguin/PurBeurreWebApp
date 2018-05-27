from django.urls import path
import re

from . import views # import views so we can use them in urls.

urlpatterns = [
    path('search/', views.search_substitute, name='search_substitute'),
    path('<int:product_id>/', views.description),
]
