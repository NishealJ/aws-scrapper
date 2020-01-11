from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    response = redirect('/app/')
    return response

def hm(request, num):
   
    return HttpResponse(num)