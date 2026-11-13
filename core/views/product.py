from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from ..models import Product


def product(request, name):

    try:
        product = Product.objects.get(title=name)
    except Product.DoesNotExist:
        return HttpResponse("Product not found")

    return render(request, "product.html", {"product": product})

def create_product(request):
    return render(request, "product_create.html")

def save_product(request):

    if request.method !="POST":
        return HttpResponseNotAllowed("This method is not allowed")

    title=request.POST.get("title")
    price=request.POST.get("price")
    description=request.POST.get("description")

    if not title or not price or not description:
        return HttpResponse("All fields are required",status=400)

    product=Product(title=title,price=price,description=description)
    product.save() # INSERT INTO PRODUCT (title,price,description) VALUES()...

    return HttpResponse(f'This is a  {title}, {price}, {description}', status=201)