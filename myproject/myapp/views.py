from django.shortcuts import render
from django.http import HttpResponse



def index(reques):
    return render(reques,"index.html")

def about(reques):
   return render(reques,"about.html")

def form(reques):
   return render(reques,"form.html")
