from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Queue


def index(reques):
    return render(reques,"index.html")

def add_person_to_queue(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        order = request.POST.get('order')
        if name and order:
            new_person = Queue.objects.create(name=name, order=order)
            return JsonResponse({'message': 'Person added to queue successfully'})
        else:
            return JsonResponse({'error': 'Please provide both name and order'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
