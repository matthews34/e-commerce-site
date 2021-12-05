from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    price = models.FloatField(validators=[MinValueValidator(0)])
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=256)

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField()
    value = models.FloatField(validators=[MinValueValidator(0)])
    
    