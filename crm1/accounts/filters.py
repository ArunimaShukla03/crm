import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class OrderFilter(django_filters.FilterSet):

    # Now, we are going to create some custom  attributes.

    start_date = DateFilter(field_name="date_created", lookup_expr="gte")

    end_date = DateFilter(field_name="date_created", lookup_expr="lte")

    company = CharFilter(field_name="company", lookup_expr='icontains')

    # "icontains" means ignore case sensitivity.

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']
        # This simply excludes these fields.