from django.db import models
from .models import *

# RELATED SET EXAMPLE
class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200, null=True)

parent_name = ParentModel.objects.first()

# Now to return all the child models related to the parent_name

parent_name.childmodel_set.all()

# Now if we want to sort, we may use

LeastToGreatest = Product.objects.all().order_by('id')
GreatestToLeast = Product.objects.all().order_by('-id')

# In case of many to many relationships (this uses double underscores or __ as it has many to many relationships)

productsFiltered = Product.objects.filter(tags__name="Sports")