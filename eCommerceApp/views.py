from django.shortcuts import render, get_object_or_404
from .models import Product 
from cart.forms import CartAddProductForm

# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {
        'products' : products,
    }

    return render(request, 'eCommerceApp/index.html', context)

def product_list(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }

    return render(request, 'eCommerceApp/products.html', context)

def product_detail(request, id):
    product =  get_object_or_404(Product, pk=id) 
    cart_product_form = CartAddProductForm()
    context = {
        'product' : product,
        'cart_product_form' : cart_product_form,
    }

    return render(request, 'eCommerceApp/single-product.html', context)