from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    address = models.CharField(max_length=256)

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField()
    value = models.FloatField()
    
    