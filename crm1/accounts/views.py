from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

# Basically formsets are used to create multiple forms within one form.

from .models import *
from .forms import *
from .urls import *
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def registerPage(request):
   form = CreateUserForm()

   if request.method=="POST":
      form = CreateUserForm(request.POST)

      if form.is_valid():
         form.save()

   context = {'form':form}

   return render(request, 'accounts/register.html', context)

def loginPage(request):
   context = {}

   return render(request, 'accounts/login.html', context)

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

    myFilter = OrderFilter(request.GET, queryset=orders)

    # We are gonna query all the orders, then throw those into this filter (myFilter) and based on our request data, we are finally going to filter this data down.

    # GET is used to retrieve data and POST is used to send data.

    orders = myFilter.qs

    # This redefines the variable "orders" and finally renders the filtered data.

    # Here, "qs" is the queryset

    context = {'customer':customer, 
               'orders':orders, 
               'total_customer_orders':total_customer_orders,
               'myFilter':myFilter}

    return render(request, 'accounts/customer.html', context)

def createOrder(request,pk_customer):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=3)

    # 'Inline formsets' have the parent (here 'Customer'), the child (here 'Order') and then the fields that we need from that respective child.

    # The 'extra' is added to show the amount of additional fields that can be added to a for.

    customer = Customer.objects.get(id=pk_customer)

    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)

    # "queryset=Order.objects.none()" is basically saying that if we have objects then don't reference them and just let it all be the new items.
    
    # form = OrderForm(initial={'customer':customer})

    # 'Instance' is used to pre-fill the form fields with data from an existing database while 'Initial' is basically initial data or used to pre-fill the form fields with default values.

    if request.method == "POST" :
       formset = OrderFormSet(request.POST,instance=customer)

       # form = OrderForm(request.POST)

       if formset.is_valid():
        formset.save()
        return redirect('/')
       
       # Here we have '/' as the URL pattern which means that it will redirect to the home page.

    context = {'formset':formset, 'item': customer}

    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk_test):

    order = Order.objects.get(id=pk_test)

    # To see a pre-filled form, we have "instance" set to order.

    form = OrderForm(instance=order)

    context = {'form':form, 'item': order}

    if request.method == "POST" :
        # If we write this POST method then it would create a new item rather than updating it so we add in the instance to avoid that. 

        # Instance is a keyword argument that takes a model in which the formset will edit.
       form = OrderForm(request.POST, instance=order)

       if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'accounts/update_form.html', context)

def deleteOrder(request, primary_key):

    order = Order.objects.get(id=primary_key)

    if request.method == "POST":
        order.delete()
        return redirect('/')        

    context={'item': order}

    return render(request, 'accounts/delete_form.html', context)