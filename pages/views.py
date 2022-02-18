from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product


# Create your views here.

def index(request):
    context ={
        'products':Product.objects.all(),
    }
    return render(request ,'pages/index.html' ,context)
    # return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return render(request ,'pages/about.html')
    # return HttpResponse('<h1> About Page</h1>')

def coffee(request):
    return render(request,'pages/coffee.html')
