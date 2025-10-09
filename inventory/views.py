from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request,'inv_home.html')

def create_product(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')


        category = Category.objects.get_or_create(id=category_id) if category_id else None

        product = Product.objects.create(
            product_name = name,
            product_category = category,
            product_price = price,
            product_qty = quantity,
        )

    categories = Category.objects.all()

    return render(request,'create_product.html',{'categories':categories})
