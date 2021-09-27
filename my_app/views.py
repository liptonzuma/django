from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def myfunctioncall(request):
    return HttpResponse('Hello world')

# Create your views here.
