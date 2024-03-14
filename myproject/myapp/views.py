from django.shortcuts import render
from django.http import HttpResponse
from .models import Queue


def index(request):
    return render(request,"index.html")

def viewqueue(request):
    return render(request,"view-queue.html")


