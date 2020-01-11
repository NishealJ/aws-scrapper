# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from scrap import books_all_scrap
# Create your views here.

def index(request):
    
    return render(request, 'csapp/index.html')

def books_all(request):

    return JsonResponse(books_all_scrap(), safe=False)
