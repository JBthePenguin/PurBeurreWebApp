#! /usr/bin/env python3
# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render
from registration.backends.default.views import RegistrationView
from .models import UserProfile
from .forms import SignupForm


# Registration View
class AppRegistrationView(RegistrationView):
    form_class = SignupForm

    def register(self, form_class):
        new_user = super(AppRegistrationView, self).register(form_class)
        user_profile = UserProfile()
        user_profile.user = new_user
        user_profile.gender = form_class.cleaned_data['gender']
        user_profile.save()
        return user_profile


# VIEWS
def my_account(request):
    message = "Page descriptive du compte my_account.html"
    return HttpResponse(message)


def wait_confirm(request):
    return render(request, 'registration/activation_email_send.html')
