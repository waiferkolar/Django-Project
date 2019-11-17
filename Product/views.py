from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def home(request):
    context = {"products":Product.objects.all(),"title":"Product Home Page"}
    return render(request,"Product/home.html",context)

def singProduct(request):
    return render(request,"Product/single.html",{"title":"Single Product Page"})
