from django.db import models

# Create your models here.
class Product(models.Model):
    count = models.IntegerField(null=False)
    img = models.ImageField(upload_to='products', blank=True, null=True)
    description = models.CharField(null=False, max_length = 100)