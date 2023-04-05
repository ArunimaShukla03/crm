from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from django.contrib.auth.models import User
# This imports the "User" model that is already built-in django.

from .models import Order

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
        ''' 
        This basically says to create a form with all the fields as that of the "Order" model. If I wanted to just have one field then I would've created a list like

        fields = ['customer', 'products']
        '''

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        # The field can be read from the docs in django.