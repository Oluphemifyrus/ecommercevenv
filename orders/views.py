from django.shortcuts import get_object_or_404, redirect
from .models import Customer, OrderItem
import json
import requests
from django.conf import settings
from django.urls import reverse
from cart.cart import Cart
from django.shortcuts import render
from django.shortcuts import render
from .forms import CustomerCreateForm
from cart.cart import Cart
from eCommerceApp.models import Product

# Create your views here.

def add_customer(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CustomerCreateForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return render(request, 'orders/payment.html',
                            {'email': customer.email, 'id':customer.id})

    else:
        form = CustomerCreateForm()

    return render(request, 'orders/create.html', {'cart':cart, 'form':form})




def save_item(request, id):
    cart = Cart(request)
    customer = get_object_or_404(Customer, pk=id)
    for item in cart:
        OrderItem.objects.create(customer=customer,
                                 product=item['product'],
                                 price=item['price'],
                                 quantity=item['quantity'])
    # clear the cart
    cart.clear()
    return redirect('eCommerceApp:product_list')





# create the Paystack instance
api_key = settings.PAYSTACK_TEST_SECRET_KEY
url = settings.PAYSTACK_INITIALIZE_PAYMENT_URL


def processpayment(request):
    
    if request.method == 'POST':
        
        customerid = request.POST.get('customerid')
        email = request.POST.get('email')
        cart = Cart(request)
        amount = cart.get_total_price() * 100
        
        
        success_url = request.build_absolute_uri(
            reverse('orders:save_item', kwargs={'id': customerid}))
        cancel_url = request.build_absolute_uri(
            reverse('orders:canceled'))

        # metadata to pass additional data that 
        # the endpoint doesn't accept naturally.
        metadata= json.dumps({"payment_id":customerid,  
                              "cancel_action":cancel_url,   
                            })

        # Paystack checkout session data
        session_data = {
            'email': email,
            'amount': int(float(amount)),
            'callback_url': success_url,
            'metadata': metadata
            }

        headers = {"authorization": f"Bearer {api_key}"}
        # API request to paystack server
        r = requests.post(url, headers=headers, data=session_data)
        response = r.json()
        if response["status"] == True :
            # redirect to Paystack payment form
            try:
                redirect_url = response["data"]["authorization_url"]
                return redirect(redirect_url, code=303)
            except:
                pass
        else:
            return render(request, 'orders/create.html', locals())
    else:
        return render(request, 'orders/create.html', locals())
    
    
def payment_canceled(request):
    return render(request, 'orders/canceled.html')

