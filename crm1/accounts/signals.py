from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Customer

# In Django, the "create" parameter is a boolean value that indicates whether an instance of a model was just created or not. Here, if the instance of the model "Customer" was created, we send a signal to the receiver, here, "customer_profile" which performs a specific function.

def customer_profile(sender, instance, created, **kwargs):

    if created:

        group = Group.objects.get(name="customer")

        instance.groups.add(group)

        # We already created the "User" model through "form.save()" thus we only need to create the associated "Customer" model now.

        Customer.objects.create(
            user = instance,
            name = instance.username
        )

        print('Profile created.')

post_save.connect(customer_profile, sender=User)
