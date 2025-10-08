from django.shortcuts import render
from .models import Products
# Create your views here.
def inventory_index(request):
    return render(request,'index.html')

def create_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')

        if product_name and product_price:
            Products.objects.create(product_name=product_name, product_price=product_price)
    return render(request,'create_product.html')