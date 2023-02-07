from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

# Create your views here.

def home(request):
    orders = Order.objects.all()

    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()

    delivered_orders = orders.filter(status='Delivered').count()

    pending_orders = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers, 'total_orders':total_orders, 'delivered_orders':delivered_orders, 'pending_orders':pending_orders}

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {
        'products':products
    })

# Here we also pass in the primary key which decides what template to return to the user.

def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()

    total_customer_orders = orders.count()

    context = {'customer':customer, 'orders':orders, 'total_customer_orders':total_customer_orders}

    return render(request, 'accounts/customer.html', context)

def createOrder(request):

    form = OrderForm()

    context = {'form':form}

    return render(request, 'accounts/order_form.html', context)
