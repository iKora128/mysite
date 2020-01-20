from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def top(request):
    ctx = {"title": "Django学習サイト"}
    return render(request, "base/top.html", ctx)

