from django.urls import path, re_path, include
from registration.backends.simple.views import RegistrationView
from . import views


urlpatterns = [
    re_path(
        r'^register/$',
        RegistrationView.as_view(form_class=views.SignupForm),
        name='registration_register'
    ),
    path('', include('registration.backends.simple.urls')),
    path('my_account/', views.my_account)
]
