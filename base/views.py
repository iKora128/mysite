from django.shortcuts import render
from django.http import HttpResponse

def top(request):
    return HttpResponse("Hello Django")