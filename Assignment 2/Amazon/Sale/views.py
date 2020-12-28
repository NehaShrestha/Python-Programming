from django.shortcuts import render
from Sale.models import *
# Create your views here.


def index(request):
    context = {
        'name': 'Neha Shrestha',
        'age': 20,
        'college': 'Deerwalk Institute of Technology'
    }
    return render(request, 'Sale/new.html', context)

