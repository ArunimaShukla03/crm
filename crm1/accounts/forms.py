from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
        ''' 
        This basically says to create a form with all the fields as that of the "Order" model. If I wanted to just have one field then I would've created a list like

        fields = ['customer', 'products']
        '''