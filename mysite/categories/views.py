from django.shortcuts import render

# Create your views here.
#categories/views.py
from products.models import Product 
from .models import Category 
def category_list(request):
    categories = Category.objects.all() #retrieve all categories 
    return render(request,'categories/category_list.html', {'categories': categories})

def category_product(request):
    categories = Category.objects.all() #retrieve all categories 
    products = Product.objects.all()
    return render(request, 'categories/category_products.html', {'categories': categories, 'products':products })












