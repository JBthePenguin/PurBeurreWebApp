#! /usr/bin/env python3
# coding: utf-8

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# SIGNUP FORM
class SignupForm(UserCreationForm):
    """ extend the UserCreationForm """
    first_name = forms.CharField(
        max_length=30, required=True, help_text='Optional.'
    )
    last_name = forms.CharField(
        max_length=30, required=True, help_text='Optional.'
    )
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.'
    )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )


def my_account(request):
    message = "Page descriptive du compte my_account.html"
    return HttpResponse(message)
