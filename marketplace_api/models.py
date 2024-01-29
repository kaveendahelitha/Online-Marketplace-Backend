from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=255, unique=True,default='')
    def __str__(self):
        return self.first_name


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True,null=False,blank=False)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    image = models.ImageField(upload_to='product/product_images',null=False,blank=False)
    name = models.CharField(max_length=255,blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name