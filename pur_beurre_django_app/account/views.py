#! /usr/bin/env python3
# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse

def my_account(request):
    message = "Page descriptive du compte my_account.html"
    return HttpResponse(message)
