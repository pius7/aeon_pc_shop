from django.db import models



class parts_url(models.Model):
    name = models.CharField(max_length=254, default='')
    url = models.CharField(max_length=254, default='')
    category = models.CharField(max_length=254, default='')
    pass

    def __str__(self):
        return self.name
        
class part(models.Model):
    product = models.ForeignKey(
        'parts_url',
        on_delete=models.CASCADE,
    )
    image = models.ImageField()
    
class info_category(models.Model):
    product = models.ForeignKey(
        'parts_url',
        on_delete=models.CASCADE,
        )
    
