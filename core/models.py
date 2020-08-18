from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class Constants:
    gender = (
        ('Male', 'Male'),
        ('Female','Female'),
        ('Others', 'Others')
    )
    CATEGORY_CHOICES = (
        ('ST', 'Shirts And Tops'),
        ('TEES', 'T-Shirts'),
        ('SK', 'Skirts'),
        ('HS', 'Hoodies&Sweatshirts')
    )
    sizechoices = (
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL')
    )

def get_url(instance,filename):
    return "item/{}".format(filename)

class person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False)
    gender = models.CharField(choices=Constants.gender , default='Female', max_length=8)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return "{0}".format(self.name)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=Constants.CATEGORY_CHOICES, max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="gallery/")
    size = models.CharField(choices=Constants.sizechoices, default='M', max_length=2)

    def __str__(self):
         return self.title

class OrderItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=Constants.CATEGORY_CHOICES, max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="gallery/")
    user = models.CharField(max_length=25)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    size = models.CharField(choices=Constants.sizechoices, default='M', max_length=2)

    def __str__(self):
         return f"{self.quantity} of {self.title} , {self.size}"






