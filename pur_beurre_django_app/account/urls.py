from django.urls import path

from . import views # import views so we can use them in urls.

urlpatterns = [
    path('my_account/', views.my_account)
]
