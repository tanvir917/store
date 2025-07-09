from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product

def calculate():
    x=1
    y=2
    return x+y

# Create your views here.
def say_hello(request):
    query_set = Product.objects.all()
    for product in query_set:
        print(product.title, product.unit_price, product.collection.title)
    return render(request, 'hello.html', { 'name': 'Tanvir', 'value': query_set.count(), 'products': query_set }) 