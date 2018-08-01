from django.db import models
from separatedvaluesfield.models import SeparatedValuesField



class parts_url(models.Model):
    name = models.CharField(max_length=254, default='')
    url = models.CharField(max_length=254, default='')
    category = models.CharField(max_length=254, default='')
    pass

    def __str__(self):
        return self.name
        
class part(models.Model):
    product = models.ForeignKey(parts_url, blank=False, related_name='part_info')
    image = models.ImageField(upload_to='images', max_length=None)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    rating = models.IntegerField(blank=False, default = 1)
    specs_categorys = SeparatedValuesField(max_length=512, token=',' , null=True)
    specs_values = SeparatedValuesField(max_length=512, token=',', null=True)
    available_amount = models.CharField(max_length=15, default='')
    available_from = models.DateField(blank=True, null=True)
    countsold= models.IntegerField(blank=False, default = 1)
    
    def __str__(self):
        return self.product.name
    
    
