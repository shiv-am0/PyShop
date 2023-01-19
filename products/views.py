from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Fetch all products from the database and pass it to the HTML template for rendering
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New Page')
