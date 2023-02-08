from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
from .urls import *

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

    if request.method == "POST" :
       form = OrderForm(request.POST)

       if form.is_valid():
        form.save()
        return redirect('/')

    context = {'form':form}

    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk_test):

    order = Order.objects.get(id=pk_test)

    # To see a pre-filled form, we have "instance" set to order.

    form = OrderForm(instance=order)

    context = {'form':form}

    if request.method == "POST" :
        # If we write this POST method then it would create a new item rather than updating it so we add in the instance to avoid that. 

        # Instance is a keyword argument that takes a model in which the formset will edit.
       form = OrderForm(request.POST, instance=order)

       if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, primary_key):

    context={}

    return render(request, 'accounts/delete_form.html', context)