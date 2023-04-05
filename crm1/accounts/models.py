from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    # This one to one field means that the user can have one customer and the customer can only have one user.

    # "blank=True" means that we can create a customer without a user attached to it.

    # "models.CASCADE" means that whenever the User is deleted, it deletes the relationship to the customer.

    name = models.CharField(max_length=200, null=True)

    phone = models.CharField(max_length=200, null=True)

    email = models.CharField(max_length=200, null=True)

    profile_pic = models.ImageField(default="random.jpeg", null = True, blank = True)

    # "auto_now_add" creates a snapshot of date and time when the customer is added.

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # We want to now see the name of the customers instead of just "Customer object(1)" in the admin panel. Thus we do the following for the same.

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )

    name = models.CharField(max_length=200, null=True)

    price = models.FloatField(null = True)

    category = models.CharField(max_length=200, null=True, choices=CATEGORY)

    description = models.CharField(max_length=200, null=True, blank=True) 

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    
    # We want the dropdown menu for "status"

    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    # This order will retain in the database even after deleting that customer as the order's cutomer will be set to NULL.

    customer = models.ForeignKey(Customer, null=True, on_delete = models.SET_NULL)

    product = models.ForeignKey(Product, null=True, on_delete = models.SET_NULL)
    
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    status = models.CharField(max_length=200, null=True, choices=STATUS)

    # As we don't have a model field that can be used to partial search, so to do that we add an additional "company" field.

    company = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.product.name

