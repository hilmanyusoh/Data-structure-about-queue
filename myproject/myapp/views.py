from django.shortcuts import render
from django.http import HttpResponse
from .queue import Queue, bakery_queue


# def simulate_bakery_queue(request):
#    bakery_queue()
#   return render(request, 'myapp/queue.html')

def simulate_bakery_queue(request):
    if request.method == 'POST':
        bakery_output = bakery_queue()
        return render(request, 'myapp/simulation_result.html', {'bakery_output': bakery_output})
    else:
        return render(request, 'bakery_queue/simulation_form.html')


# Create your views here.
# def index(reques):
#    return render(reques,"index.html")

# def about(reques):
#   return render(reques,"about.html")

# def form(reques):
#   return render(reques,"form.html")
