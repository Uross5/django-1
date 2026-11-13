from django.http import HttpResponse
from django.shortcuts import render
from ..models import Product

def home(request):

    return render(request, "index.html",
     { "products": Product.objects.order_by('-id')[:9]
     } )

def about(request):
    return HttpResponse("Not possible to show the page", status=404)