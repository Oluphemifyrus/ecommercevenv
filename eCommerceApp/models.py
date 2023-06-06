from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    availableUnit = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

